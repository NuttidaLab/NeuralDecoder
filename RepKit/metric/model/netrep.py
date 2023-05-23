import numpy as np

from ...lib.netrep_local.metrics.stochastic import GaussianStochasticMetric
from ...lib.netrep_local.metrics.stochastic import EnergyStochasticMetric
from ...lib.netrep_local.multiset import pairwise_distances

class GSM:

    def __init__(self):
        pass

    def measure(self, data, metric, alpha = 1):

        processed_data = self.process(data)

        distances = pairwise_distances(GaussianStochasticMetric(alpha), processed_data, verbose=True)

        return distances
    
    def get_means_and_covs(self, X, y):
        classes = np.unique(y)
        means = np.stack([np.mean(X[y==labels], 0) for labels in classes], 0) # Meaning: compute the mean of each class
        covs = np.stack([np.cov(X[y==labels].T) for labels in classes], 0) # Meaning: compute the covariance of each class
        return means, covs

    def process(self, data, downsample=4):
        all_x = np.stack([x for x,y in data])
        all_y = np.stack([y for x,y in data])

        all_x = all_x[:, :, ::downsample]

        processed = []

        for i in range(len(all_x)):
            means, covs = self.get_means_and_covs(all_x[i], all_y[i])
            processed.append((means, covs))
        
        return processed
    

class ESM:

    def __init__(self, verbose = True):
        self.verbose = verbose

        
    def measure(self, data, metric, alpha = 1):
        processed_data = self.process(data)
        distances = pairwise_distances(EnergyStochasticMetric(), processed_data, verbose=True)
        return distances

    def reshape_networks_by_class(self, all_x, all_y, classes):
        """Returns list of Networks in shape [(class, sample, feature), (class, sample, feature), ...]"""
        
        all_x_by_class = []
        all_y_by_class = []

        # iterate over all networks
        for i in range(len(all_x)):
            # get the network
            X = all_x[i]
            Y = all_y[i]

            # split the network by class
            X_by_class = [X[Y==label] for label in classes]
            Y_by_class = [Y[Y==label] for label in classes]

            # append the network to the list of networks
            all_x_by_class.append(X_by_class)
            all_y_by_class.append(Y_by_class)
        
        # return the list of networks
        return all_x_by_class, all_y_by_class

    def get_min_samples_per_class(self, all_x_by_class):
        """Works accross all networks and returns the minimum number of samples per class"""

        minimum_samples_per_class = float('inf')

        # iterate over all networks
        for net_id, network in enumerate(all_x_by_class):
            
            # iterate over all classes
            for class_id, classes in enumerate(network):

                # get the number of samples in the class
                sample_length = len(classes)

                if self.verbose: print(f"for network {net_id}| class {class_id} | found:  {sample_length} samples")

                # check if the number of samples is less than the current minimum
                if sample_length < minimum_samples_per_class:
                    minimum_samples_per_class = sample_length
        
        if self.verbose: print(f"Minimum samples per class over all networks found: {minimum_samples_per_class}")

        # return the minimum number of samples per class
        return minimum_samples_per_class
    
    
    def slice_by_samples(self, all_x_by_class, n_min_samples):
        """Returns a list of networks in shape np.array([(class, n_minsamples, feature), (class, n_minsamples, feature), ...])"""

        all_x_sliced = []

        # iterate over all networks
        for network in all_x_by_class:
            net_t = []
            # iterate over all classes
            for classes in network:

                # slice the class by the minimum number of samples
                net_t.append(classes[:n_min_samples])
            
            # append the network to the list of networks
            all_x_sliced.append(np.array(net_t))

        if self.verbose: print(f"Succesfully sliced the networks: {all_x_sliced[0].shape}")

        # return the list of networks
        return all_x_sliced

    def process(self, data):
        """Preprocess data for RSA analysis
        They are segrigated by class (by using ground truth y), then by sample, then by feature
        example shapes (Xi, Xj): ((4, 225, 2), (4, 225, 2))
        Final digested data has to be a [np.array, np.array]
        """

        # get the data
        all_x = np.stack([x for x,y in data])
        all_y = np.stack([y for x,y in data])

        classes = np.unique(all_y[0])

        # reshape the networks by class
        all_x_by_class, all_y_by_class = self.reshape_networks_by_class(all_x, all_y, classes)

        # get the minimum number of samples per class
        n_min_samples = self.get_min_samples_per_class(all_x_by_class)

        # slice the networks by the minimum number of samples
        all_x_sliced = self.slice_by_samples(all_x_by_class, n_min_samples)
        
        return all_x_sliced
        
