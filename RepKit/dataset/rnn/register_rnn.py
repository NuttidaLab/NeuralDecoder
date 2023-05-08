from ..dataset_parent import RepKitDataset
import numpy as np

class register(RepKitDataset):
    def __init__(self, data: np.ndarray, labels: np.ndarray = None):
        self.data = data
        self.labels = labels
        super().__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx] if self.labels is not None else None