# to test if monkee can handle this
# Only 3 baseline networks utilized
# Only 2 samples per network

import os, sys; sys.path.append(os.path.abspath('./'))

from inspector.rsa import ESM

# Crawl the data directory
import os
data_dir = r'.\data\baseline'
data_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.mat')]

samples = 2
flattens = 60000

# loop over the files
import scipy.io

network_X = []
network_y = []

for f in data_files[:3]:
    data = scipy.io.loadmat(f)
    test_x = data['test_x']
    test_out = data['test_out']

    network_X.append(test_x)
    network_y.append(test_out)

len(network_X), len(network_y)

network_X[0].shape, network_y[0].shape

network_X[1].shape, network_y[1].shape

x_1 = network_X[0]
x_2 = network_X[1]
x_3 = network_X[2]

import numpy as np

# Assuming X1 and X2 are RNN models of shape (4, 50, 200, 300)
# Flatten the time steps and neuron dimensions of each RNN model
X1_flat = np.reshape(x_1, (x_1.shape[0], x_1.shape[1], -1))
X2_flat = np.reshape(x_2, (x_2.shape[0], x_2.shape[1], -1))
X3_flat = np.reshape(x_3, (x_3.shape[0], x_3.shape[1], -1))

# slice only the first samples
X1_flat = X1_flat[:,:samples,:flattens]
X2_flat = X2_flat[:,:samples,:flattens]
X3_flat = X3_flat[:,:samples,:flattens]

print(X1_flat.shape, X2_flat.shape, X3_flat.shape)

netrep_metric = ESM(verbose = True)
ingestion_report = netrep_metric.ingest([X1_flat, X2_flat, X3_flat], None, preprcessed = True)
energy_distance = netrep_metric.score()

# save the distance matrix
np.save('baseline_flattened_3_nets_2_samples.npy', energy_distance)


