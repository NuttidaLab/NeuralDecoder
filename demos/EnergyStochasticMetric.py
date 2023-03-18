if __name__ == "__main__":
    # Setting working direcotry to the root of the project for the purpose of demonstration 
    import os, sys; os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.append('..')

# Importing the required packages
from inspector.rsa import ESM
from inspector.dataset import SyntheticNetworks


# create 10 synthetic networks
network_generator = SyntheticNetworks()
networks_X, networks_y = network_generator.generate(networks=10)

# create an RSA object
netrep_metric = ESM()
ingestion_report = netrep_metric.ingest(networks_X, networks_y)
digestion_report = netrep_metric.digest()
energy_distance = netrep_metric.score(verbose=True)

netrep_metric.plot()