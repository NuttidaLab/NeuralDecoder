import sklearn.datasets
import numpy as np

class SyntheticNetworks():
    def __init__(self) -> None:
        pass

    def generate(self, networks = 3):
        # seed = 42069
        n_samples = 2048
        n_classes = 4  # Number of stimuli M
        n_features = 2  # Dimensionality of responses N

        # rng = np.random.default_rng(seed)

        X , y = [], []

        for i in range(networks):
            # Generate a new dataset
            _X, _y = sklearn.datasets.make_classification(
                n_samples=n_samples, 
                n_features=n_features, 
                n_informative=n_features, 
                n_redundant=0, 
                n_repeated=0, 
                n_classes=n_classes, 
                n_clusters_per_class=1, # Meaning: each class is a single cluster
                # random_state=seed,
            )
            X.append(_X)
            y.append(_y)

        return X, y