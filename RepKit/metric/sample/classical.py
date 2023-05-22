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
            nx_i, _ = data[i]
            nx_j, _ = data[j]
            distances[i, j] = pdist(np.stack([nx_i, nx_j]), metric=metric)
            
        distances += distances.T
        
        # return the distance matrix
        return distances