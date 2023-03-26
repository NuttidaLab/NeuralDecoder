from typing import Tuple
import numpy.typing as npt
import numpy as np

from ..metric import Metric
from ..utility import plot_distmat

from sklearn.metrics import pairwise_distances

class Classical(Metric):
    """Classical RSA metric
    
    Supported: 
        - l1: Manhattan distance
        - l2: Euclidean distance
        - minkowski: Minkowski distance
        - cosine: Cosine similarity
        - correlation: Correlation coefficient
        - chebyshev: Chebyshev distance
        - braycurtis: Bray-Curtis distance
        - canberra: Canberra distance
        - nan_euclidean: Euclidean distance with NaNs

    """

    def __init__(self, verbose = True):
        super().__init__(verbose)


    def digest(self):
        """For the moment, downsamples to 75 timesteps due to a limitation in the netrep package
        """

        # check if the data has already been digested
        if self.data["digested_flag"]:
            if self.verbose: print("Data already digested, skipping digestion")
            return "TBD Digestion Report"

        X_all = self.data['X']
        # Y_all = self.data['y'] # Y is not used in the metric right now, this needs to be fixed

        self.data['digested_networks'] = X_all.reshape(X_all.shape[0], -1)

        if self.verbose: print(f"Successfully digested data, available in self.data['digested_networks']")

        # set the digested flag
        self.data["digested_flag"] = True
        
        # return the report of digested networks
        return "TBD Digestion Report"

    def score(self, metric = "l1", networks = False):
        """Compute the RSA score for the given metric

        All different metrics implementations and their corresponding names are listed below:

            Manhattan distance: 'manhattan', 'cityblock', 'l1'
            Euclidean distance: 'euclidean', 'l2', 'sqeuclidean'
            Minkowski distance: 'minkowski', 'wminkowski'
            Correlation-based distance: 'correlation', 'cosine'
            Chebyshev distance: 'chebyshev'
            Mahalanobis distance: 'mahalanobis'
            Binary distance measures: 'hamming', 'jaccard', 'dice', 'kulsinski', 'matching', 'rogerstanimoto', 'russellrao', 'sokalmichener', 'sokalsneath', 'yule'
            Other distance measures: 'braycurtis', 'canberra', 'nan_euclidean', 'seuclidean', 'haversine'
        
        """

        if not networks: networks = self.data['digested_networks']

        # good stuffs
        supported = [
            'l1', 
            'l2',
            'minkowski',
            'cosine', 
            'correlation',
            'chebyshev', 
            'braycurtis',
            'canberra',
            'nan_euclidean'
        ]

        # check if the metric is supported
        if metric not in supported:
            raise ValueError(f"Unsupported metric: {metric}")
        
        # compute the distance matrix
        distmat_energy = pairwise_distances(networks, networks, metric=metric)

        # store the distance matrix
        self.data['distance_matrix'] = distmat_energy
        self.metric = metric

        # return the distance matrix
        return distmat_energy
    
    def plot(self, title=f"Classical Stochastic Metric", out_path=None):
        """Plot the RSA score"""
        title = f"{self.metric} distance"
        plot_distmat(self.data['distance_matrix'], title=title, out_path=out_path)