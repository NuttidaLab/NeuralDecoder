from .rsa import GSM, ESM, Classical
from .utility import export_distmat
import tqdm
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

class ModelByModel:

    def __init__(self, X, y, verbose=True):
        """Register the data to be used for the analysis.

        Parameters
        ----------
        X : array-like of shape (models, n_samples, n_features)
            The data matrix.

        y : array-like of shape (models, n_samples)
            The target vector.

        Returns
        -------
        self : object
            Returns the instance itself.
        """

        self.X = X
        self.y = y
        self.distances = []
        self.verbose = verbose
    
    def map_metric_options(self, metric):
        """Get the current metric object.

        Parameters
        ----------
        metric : str
            The metric to be used for the similarity matrix.

        Returns
        -------
        metric object : object
            Returns the current_metric object.
        """

        if metric in ["l1", "l2", "minkowski", "cosine", "correlation", "chebyshev", "braycurtis", "canberra", "nan_euclidean"]:
            current_metric = Classical(verbose=False)
        
        elif metric == "gsm":
            current_metric = GSM(verbose=False)
        
        elif metric == "esm":
            current_metric = ESM(verbose=False)

        else:
            raise ValueError(f"Metric {metric} not supported.")

        return current_metric
    
    def score(self, metric=["l2"]):
        """Compute the similarity matrix of the data using the specified metric.

        Parameters
        ----------
        metric : str or list of str, default = ["l2"]
            The metric to be used for the similarity matrix.

        Returns
        -------
        self : object
            Returns the instance itself.

        Notes
        -----
        If metric is one of these, use Classical RSA: 
            - l1: Manhattan distance
            - l2: Euclidean distance
            - minkowski: Minkowski distance
            - cosine: Cosine similarity
            - correlation: Correlation coefficient
            - chebyshev: Chebyshev distance
            - braycurtis: Bray-Curtis distance
            - canberra: Canberra distance
            - nan_euclidean: Euclidean distance with NaNs

        If metric is one of these, use GSM RSA:
            - gsm: NetRep

        If metric is one of these, use ESM RSA:
            - esm: NetRep
        """

        if isinstance(metric, list):
            self.metric = metric
        else:
            self.metric = [metric]

        for metric in tqdm.tqdm(self.metric):
            current_metric = self.map_metric_options(metric)
            current_metric.ingest(self.X, self.y)
            current_metric.digest()
            self.distances.append(current_metric.score(metric=metric))
        
        if self.verbose: print(f"Scored {len(self.metric)} metrics. Available in self.distances")
        
        return self.distances
    
    def export(self, out_dir = r"out", format = r"eps", normalize = True, color_map_hex = []):
        
        if normalize:
            self.distances = [result / np.max(result) for result in self.distances]

        if color_map_hex:
            boundaries = [0.0, 1.0]
            hex_colors = color_map_hex
            colors=list(zip(boundaries, hex_colors))
            custom_color_map = LinearSegmentedColormap.from_list(
                name='custom_navy',
                colors=colors,
            )
            cmap = custom_color_map
        else:
            cmap = 'coolwarm'

        for i, metric in enumerate(self.metric):
            export_distmat(self.distances[i], out_dir, metric, annot = True, format = format, color_map_hex = cmap)

        if self.verbose: print(f"Exported {len(self.metric)} metrics to {out_dir}.")





