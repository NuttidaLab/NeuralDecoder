from .decomposer_parent import RepKitDecomposer

from sklearn.manifold import MDS as sklearn_MDS
from sklearn.decomposition import PCA as sklearn_PCA

import scprep

class mds(RepKitDecomposer):
    def __init__(self):
        super().__init__()

    def decompose(self, components,  distances = None):
        if distances is None:
            distances = self.metric.distances
        self.engine = sklearn_MDS(n_components=components, metric=True, dissimilarity='precomputed', normalized_stress="auto")
        self.embedding = self.engine.fit_transform(distances)
        return self
    
    def plot(self, labels = None, title = "MDS", label_prefix = "MDS"):
        return scprep.plot.scatter2d(self.embedding, 
                                     c = labels,
                                     title=title, 
                                     label_prefix=label_prefix,
                                     # filename="figs/mds/"+ metric_lbls[i] + ".png",
                                     legend_loc = "best")

class pca(RepKitDecomposer):
    def __init__(self):
        super().__init__()

    def decompose(self, components,  distances = None):
        if distances is None:
            distances = self.metric.distances
        self.engine = sklearn_PCA(n_components=components)
        self.embedding = self.engine.fit_transform(distances)
        return self
    
    def plot(self, labels = None, title = "PCA", label_prefix = "PCA"):
        return scprep.plot.scatter2d(self.embedding, 
                                     c = labels,
                                     title=title, 
                                     label_prefix=label_prefix,
                                     # filename="figs/mds/"+ metric_lbls[i] + ".png",
                                     legend_loc = "best")