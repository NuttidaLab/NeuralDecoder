from ..decomposer import mds

class RepKitSpace:

    dataset = None
    metric = None
    decomposer = None
    distances = None
    available_engines = {
        'mds': mds
    }

    def __init__(self) -> None:
        pass

    def measure(self, data, metric):
        raise NotImplementedError
    
    def plot_distance(self):
        self.metric.plot()
        return self

    def plot_embedding(self, labels = None, title = "MDS", label_prefix = "MDS"):
        self.decomposer.plot(labels = labels, title = title, label_prefix = label_prefix)
        return self