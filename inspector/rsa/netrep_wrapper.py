
from inspector import Metric
from inspector.utility import plot_distmat

from netrep.metrics.stochastic import EnergyStochasticMetric
from netrep.multiset import pairwise_distances

class NetRep(Metric):
    '''Base class for NetRep wrapper classes'''

    def __init__(self, verbose = True):
        super().__init__(verbose)

    def score(self, networks = False):
        '''Compute the netrep score'''

        metric = EnergyStochasticMetric()
        if not networks: networks = self.data['digested_networks']
        distmat_energy = pairwise_distances(metric, networks, verbose=self.verbose)

        self.data['distance_matrix'] = distmat_energy

        return distmat_energy

    def plot(self):
        '''Plot the RSA score'''
        plot_distmat(self.data['distance_matrix'], title="Distance Metric")
    