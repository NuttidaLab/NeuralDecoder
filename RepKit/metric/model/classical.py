from scipy.spatial.distance import pdist
import numpy as np
import itertools
from tqdm import tqdm

class Classical:
    """https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html"""

    def __init__(self) -> None:
        pass

    def measure(self, data, metric: str):

        n_data = len(data)

        distances = np.zeros((n_data, n_data))

        for i,j in tqdm(itertools.combinations(range(n_data), 2), total = n_data * (n_data - 1) / 2):
            # Get X for 2 networks being compared
            nx_i, _ = data[i]
            nx_j, _ = data[j]

            # Average samplewise distance for networks i and j
            samplewise_dists = []
            for id_sample in range(len(nx_i)):
                t = np.stack([nx_i[id_sample], nx_j[id_sample]])
                if len(t.shape) == 1:
                    t = np.expand_dims(t, axis=0)
                t_dist = pdist(t, metric=metric)
                samplewise_dists.append(t_dist)
            
            # drop all NaNs from samplewise_dists
            samplewise_dists = np.array(samplewise_dists)
            samplewise_dists = samplewise_dists[~np.isnan(samplewise_dists)]
            
            # Check if Samplewise_dists is empty
            if len(samplewise_dists) == 0:
                distances[i, j] = np.nan # If empty, setting distance to nan, but what to do ideally?
            else:
                distances[i, j] = np.mean(samplewise_dists)
        
        distances += distances.T
        
        # return the distance matrix
        return distances