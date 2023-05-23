from .space_parent import RepKitSpace
from ..metric import sample_metric

class sample_space(RepKitSpace):

    def __init__(self) -> None:
        self.metric = sample_metric()
        super().__init__()


    