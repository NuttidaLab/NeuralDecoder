# Setting working direcotry to the root of the project for the purpose of demonstration 
import os, sys; sys.path.append(os.path.abspath('./'))

# Importing the required packages
from inspector.rsa import Classical
from inspector.dataset import DataLoader

# Load the first 5 baselines from directory
dataloader = DataLoader()
networks_X, networks_y = dataloader.flow_from_mat(data_dir = os.path.abspath(r'.\data\baseline'), n_networks = 5)

print(networks_X.shape, networks_y.shape)

# create an GSM object
netrep_metric = Classical()
ingestion_report = netrep_metric.ingest(networks_X, networks_y)
digestion_report = netrep_metric.digest()

# Supported: 
#     - l1: Manhattan distance
#     - l2: Euclidean distance
#     - minkowski: Minkowski distance
#     - cosine: Cosine similarity
#     - correlation: Correlation coefficient
#     - chebyshev: Chebyshev distance
#     - braycurtis: Bray-Curtis distance
#     - canberra: Canberra distance
#     - nan_euclidean: Euclidean distance with NaNs

energy_distance = netrep_metric.score(metric="l2")

netrep_metric.plot()