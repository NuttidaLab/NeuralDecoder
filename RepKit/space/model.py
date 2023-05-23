from .space_parent import RepKitSpace
from ..metric import model_metric

class model_space(RepKitSpace):

    def __init__(self) -> None:
        self.metric = model_metric()
        super().__init__()
    