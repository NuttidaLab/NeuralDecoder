from inspector.rsa.netrep_wrapper import NetRep
import numpy as np
from inspector.utility import plot_distmat

class ESM(NetRep):
    '''Energy Stochastic Metric'''

    def __init__(self, verbose = True):
        super().__init__(verbose)


    def reshape_networks_by_class(self, X_all, Y_all, n_classes):
        '''Returns list of Networks in shape [(class, sample, feature), (class, sample, feature), ...]'''

        X_all_by_class = []
        Y_all_by_class = []

        # iterate over all networks
        for i in range(len(X_all)):
            # get the network
            X = X_all[i]
            Y = Y_all[i]

            # split the network by class
            X_by_class = [X[Y==i] for i in range(n_classes)]
            Y_by_class = [Y[Y==i] for i in range(n_classes)]

            # append the network to the list of networks
            X_all_by_class.append(X_by_class)
            Y_all_by_class.append(Y_by_class)
        
        # return the list of networks
        return X_all_by_class, Y_all_by_class

    def get_min_samples_per_class(self, X_all_by_class):
        '''Works accross all networks and returns the minimum number of samples per class'''

        minimum_samples_per_class = float('inf')

        # iterate over all networks
        for net_id, network in enumerate(X_all_by_class):
            
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
    
    
    def slice_by_samples(self, X_all_by_class, n_min_samples):
        '''Returns a list of networks in shape np.array([(class, n_minsamples, feature), (class, n_minsamples, feature), ...])'''

        X_all_sliced = []

        # iterate over all networks
        for network in X_all_by_class:
            net_t = []
            # iterate over all classes
            for classes in network:

                # slice the class by the minimum number of samples
                net_t.append(classes[:n_min_samples])
            
            # append the network to the list of networks
            X_all_sliced.append(np.array(net_t))

        if self.verbose: print(f"Succesfully sliced the networks: {X_all_sliced[0].shape}")

        # return the list of networks
        return X_all_sliced

    def digest(self):
        '''Preprocess data for RSA analysis
        They are segrigated by class (by using ground truth y), then by sample, then by feature
        example shapes (Xi, Xj): ((4, 225, 2), (4, 225, 2))
        Final digested data has to be a [np.array, np.arry]
        '''

        # check if the data has already been digested
        if self.data["digested_flag"]:
            if self.verbose: print("Data already digested, skipping digestion")
            return "TBD Digestion Report"

        # get the data
        X_all = self.data['X']
        Y_all = self.data['y']
        n_classes = len(np.unique(Y_all[0]))

        # reshape the networks by class
        X_all_by_class, Y_all_by_class = self.reshape_networks_by_class(X_all, Y_all, n_classes)

        # get the minimum number of samples per class
        n_min_samples = self.get_min_samples_per_class(X_all_by_class)

        # slice the networks by the minimum number of samples
        X_all_sliced = self.slice_by_samples(X_all_by_class, n_min_samples)

        # store the digested networks
        self.data['digested_networks'] = X_all_sliced

        if self.verbose: print(f"Successfully digested data, available in self.data['digested_networks']")
        
        # set the digested flag
        self.data["digested_flag"] = True
        
        # return the report of digested networks
        return "TBD Digestion Report"
    
    def plot(self):
        '''Plot the RSA score'''
        plot_distmat(self.data['distance_matrix'], title="Energy Stochastic Metric")