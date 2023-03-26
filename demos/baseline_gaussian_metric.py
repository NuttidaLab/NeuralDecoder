# Setting working direcotry to the root of the project for the purpose of demonstration 
import os, sys; sys.path.append(os.path.abspath('./'))

# Importing the required packages
from inspector.rsa import GSM
from inspector.dataset import DataLoader

# Load the first 5 baselines from directory
dataloader = DataLoader()
networks_X, networks_y = dataloader.flow_from_mat(data_dir = os.path.abspath(r'.\data\baseline'), n_networks = 5)

print(networks_X.shape, networks_y.shape)

# create an GSM object
netrep_metric = GSM()
ingestion_report = netrep_metric.ingest(networks_X, networks_y)
digestion_report = netrep_metric.digest()
energy_distance = netrep_metric.score()

netrep_metric.plot()