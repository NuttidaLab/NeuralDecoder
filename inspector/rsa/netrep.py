
from inspector import Metric
from inspector.utility import plot_distmat

from netrep.metrics.stochastic import EnergyStochasticMetric
from netrep.multiset import pairwise_distances

import numpy as np

class NetRep(Metric):
    '''Base class for NetRep wrapper classes'''

    def __init__(self):
        super().__init__()

    def score(self, verbose=False):
        '''Compute the netrep score'''

        metric = EnergyStochasticMetric()
        distmat_energy = pairwise_distances(metric, self.data['digested_networks'], verbose=verbose)

        self.data['distance_matrix'] = distmat_energy

        return distmat_energy

class ESM(NetRep):
    '''Energy Stochastic Metric'''

    def __init__(self):
        super().__init__()

    def digest(self):
        '''Preprocess data for RSA analysis
        They are segrigated by class (by using ground truth y), then by sample, then by feature
        example shapes (Xi, Xj): ((4, 225, 2), (4, 225, 2))
        '''

        # TO DO LATER: make this more general
        # digested_data = self.digested_data['models'] = {}

        # # register meta-data
        # self.digested_data['models']['n_networks'] = len(self.data['X'])
        # self.digested_data['labels'] = np.unique(self.data['y'])
        # self.digested_data['n_classes'] = len(self.data['labels'])
        # self.data['min_samples_per_class'] = min([len(y[y==c]) for c in self.data['n_classes']])

        n_netowrks = len(self.data['X'])

        # find the lowest number of samples of y class in X
        # this is the number of samples we will use for each class
        min_samples_per_class = float('inf')
        for i in range(n_netowrks):
            y_t = self.data['y'][i]
            min_samples_per_class = min([len(y_t[y_t==c]) for c in np.unique(y_t)])

            # replace the min_samples_per_class if the current network has a lower number of samples
            if min_samples_per_class < min_samples_per_class:
                min_samples_per_class = min_samples_per_class

        print(f'found the minimum samples to be: {min_samples_per_class} samples per class')

        all_digested_networks = []

        for i in range(n_netowrks):

            # get the data for the ith network
            X = self.data['X'][i]
            y = self.data['y'][i]

            n_classes = len(np.unique(y))

            digested_x = [X[y==i] for i in range(n_classes)] # Meaning: digested_x is a list of the data for each class
            digested_x = np.stack([x[:min_samples_per_class] for x in digested_x], 0) # Meaning: take the first samples_per_class samples for each class

            all_digested_networks.append(digested_x)
        
        print(f"succesfully digested {n_netowrks} networks to {n_classes} classes with {len(digested_x[0])} samples each")
        
        self.data['digested_networks'] = all_digested_networks

        # TO DO LATER: return a report of the preprocessing

    def plot(self):
        '''Plot the RSA score'''
        plot_distmat(self.data['distance_matrix'])
        pass


class GSM:
    def __init__(self) -> None:
        pass

    # TBD