# Setting working direcotry to the root of the project for the purpose of demonstration 
import os, sys; sys.path.append(os.path.abspath('./'))

# Importing the required packages
from inspector.dataset import DataLoader
from inspector import ModelByModel

# Load the first 5 baselines from directory
dataloader = DataLoader()
networks_X, networks_y = dataloader.flow_from_mat(data_dir = r'.\data\baseline', n_networks = 5)

# create an GSM object
metric = ModelByModel(networks_X, networks_y, verbose=False)

# compute the similarity matrix using the specified metric
distances = metric.score(metric = ["l2", "l1"])

# export the file to the desired directory in desired format
# Only 2 tone gradients are supported for now in color_map_hex
metric.export(out_dir = r"demos/out", format = r"png", normalize = True, color_map_hex=['#060047', '#FF5F9E'])