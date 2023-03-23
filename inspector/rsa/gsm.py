from typing import Tuple
import numpy.typing as npt
import numpy as np

from inspector.rsa.netrep_wrapper import NetRep
import numpy as np
from inspector.utility import plot_distmat

from netrep.metrics.stochastic import GaussianStochasticMetric

class GSM(NetRep):
    def __init__(self, verbose = True):
        super().__init__(verbose)

    def get_means_and_covs(self, X, y):
        """Helper method that computes class-conditional means and covariances."""
        
        classes = np.unique(y)
        means = np.stack([np.mean(X[y==labels], 0) for labels in classes], 0) # Meaning: compute the mean of each class
        covs = np.stack([np.cov(X[y==labels].T) for labels in classes], 0) # Meaning: compute the covariance of each class
        return means, covs

    def digest(self):

        # check if the data has already been digested
        if self.data["digested_flag"]:
            if self.verbose: print("Data already digested, skipping digestion")
            return "TBD Digestion Report"

        X_all = self.data['X']
        Y_all = self.data['y']

        self.data['digested_networks'] = []

        for i in range(len(X_all)):
            means, covs = self.get_means_and_covs(X_all[i], Y_all[i])
            self.data['digested_networks'].append((means, covs))

        if self.verbose: print(f"Successfully digested data, available in self.data['digested_networks']")

        # set the digested flag
        self.data["digested_flag"] = True
        
        # return the report of digested networks
        return "TBD Digestion Report"

    def score(self):
        metric = GaussianStochasticMetric(1)
        return super().score(metric)
    
    def plot(self, title="Gaussian Stochastic Metric", out_path=None):
        '''Plot the RSA score'''
        plot_distmat(self.data['distance_matrix'], title=title, out_path=out_path)