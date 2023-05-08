from ..dataset_parent import RepKitDataset

import scipy
import numpy as np

class flow(RepKitDataset):
    def __init__(self, data_dir: str, n_networks: int = None, preprocess: str = None) -> None:
        self.paths = self._crawl_dir(data_dir, n_networks)
        # preprocess:
        #     avg_neurons 
        #     avg_time_facing (avg neurons and time facing)
        #     alex
        self.preprocess = preprocess


    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        data = scipy.io.loadmat(self.paths[idx])
        x = data['test_x']
        x = x.reshape(-1, x.shape[-2], x.shape[-1])
        y = self._make_labels(data['test_out'])

        if self.preprocess == 'avg_time_facing':
            x = np.average(x, axis=1).T
        elif self.preprocess == 'avg_neurons':
            x = np.average(x, axis=1)
        elif self.preprocess == 'time_facing':
            x = x.transpose(2,0,1)

        return x, y

    def _make_labels(self, x):
        labels = x[:, :, -50:]
        labels = np.average(labels, axis=2).reshape(-1)
        labels[labels > 0] = 1
        labels[labels < 0] = -1
        return labels

