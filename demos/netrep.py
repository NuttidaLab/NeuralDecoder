import sys
sys.path.append('../../')

from inspector.rsa.netrep import ESM
from inspector.dataset import SyntheticNetworks

network_generator = SyntheticNetworks()

# create a synthetic dataset

X, y = network_generator.generate(networks=10)

# create an ESM object
netrep_metric = ESM()

netrep_metric.ingest(X, y)

netrep_metric.digest()

energy_distance = netrep_metric.score()

netrep_metric.plot()