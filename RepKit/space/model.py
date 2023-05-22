from .space_parent import RepKitSpace
from ..metric import model_metric

class model_space(RepKitSpace):

    def __init__(self) -> None:
        self.metric = model_metric()
        super().__init__()

    def measure(self, data, metric):
        self.dataset = data
        self.metric.measure(data, metric)
        return self
    
    def decompose(self, engine, components):
        self.decomposer = self.available_engines[engine]()
        self.decomposer.metric = self.metric
        self.decomposer.decompose(components = components)
        return self
    