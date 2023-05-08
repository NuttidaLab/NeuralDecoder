from scipy.spatial.distance import pdist
import numpy as np
import itertools
from tqdm import tqdm

class Classical:
    """https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html"""

    supported = [
        'braycurtis',
        'canberra',
        'chebyshev',
        'cityblock',
        'correlation',
        'cosine',
        'dice',
        'euclidean',
        'hamming',
        'jaccard',
        'jensenshannon',
        'kulczynski1',
        'mahalanobis',
        'matching',
        'minkowski',
        'rogerstanimoto',
        'russellrao',
        'seuclidean',
        'sokalmichener',
        'sokalsneath',
        'sqeuclidean',
        'yule'
    ]

    def __init__(self) -> None:
        super().__init__()

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
                samplewise_dists.append(pdist(np.stack([nx_i[id_sample], nx_j[id_sample]]), metric=metric))
            distances[i, j] = np.mean(samplewise_dists)
        distances += distances.T
        
        # return the distance matrix
        return distances