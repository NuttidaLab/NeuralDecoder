# Setting working direcotry to the root of the project for the purpose of demonstration 
import os, sys; sys.path.append(os.path.abspath('./'))

# Importing the required packages
from inspector.rsa import ESM
from inspector.dataset import SyntheticNetworks

# create 10 synthetic networks
network_generator = SyntheticNetworks()
networks_X, networks_y = network_generator.generate(networks=11)

# create an RSA object
netrep_metric = ESM()
ingestion_report = netrep_metric.ingest(networks_X, networks_y)
digestion_report = netrep_metric.digest()
energy_distance = netrep_metric.score()

netrep_metric.plot()