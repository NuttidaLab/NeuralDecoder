from ..decomposer import mds, pca

class RepKitSpace:

    dataset = None
    metric = None
    decomposer = None
    distances = None
    available_engines = {
        'mds': mds,
        'pca': pca
    }

    def __init__(self) -> None:
        pass

    def measure(self, data, metric):
        raise NotImplementedError
    
    def plot_distance(self):
        self.metric.plot()
        return self

    def plot_embedding(self, labels = None):
        self.decomposer.plot(labels = labels)
        return self