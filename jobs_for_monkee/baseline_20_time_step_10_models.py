import os, sys; sys.path.append(os.path.abspath('../')); sys.path.append(os.path.abspath('./'))

import scipy.io
from inspector.rsa import ESM

from tqdm import tqdm
import numpy as np

data_dir = os.path.abspath(r'..\data\baseline')
data_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.mat')]

n_networks = 10

network_X = []
network_y = []

for f in data_files[:n_networks]:
    data = scipy.io.loadmat(f)
    test_x = data['test_x']
    test_out = data['test_out']

    network_X.append(test_x)
    network_y.append(test_out)

network_X = np.array(network_X)
network_y = np.array(network_y)

print(network_X.shape, len(network_y))

network_X_transposed = network_X.transpose(4, 0, 1, 2, 3)
network_X_transposed.shape

frame_limit = 20

distance_matrix_per_time_step = []
for frame in tqdm(network_X_transposed[:frame_limit], desc="Overall progress"):
    netrep_metric = ESM(verbose = True)
    ingestion_report = netrep_metric.ingest(frame, None, preprcessed = True)
    energy_distance = netrep_metric.score()
    distance_matrix_per_time_step.append(energy_distance)

distance_matrix_per_time_step = np.array(distance_matrix_per_time_step)

# save the distance matrix
np.save("baseline_energy_dist_20_time_step_10_models.npy", distance_matrix_per_time_step)












