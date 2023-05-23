2: Basic Usage and API
======================

In this tutorial, we will demonstrate how to use RepKit to load and inspect a set of networks. We will use the RepKit `rnn` module to load a set of networks from a directory, and then inspect the shape of each network in the set.

Understanding RepKitDataset
---------------------------

All datasets used in RepKit are a child of the `RepKitDatasetClass` which inturn is a child of `torch.utils.data.Dataset`.


Importing the necessary modules
-------------------------------

First, we need to import the necessary modules. In this case, we only need to import the `rnn` module from `RepKit.dataset`:

.. code-block:: python

   from RepKit.dataset import rnn

Loading the networks
---------------------

Next, we can load the networks using the `rnn.flow()` function and create a PyTorch DataLoader object for the networks using the `get_dataloader()` function:

.. code-block:: python

   networks = rnn.flow("data/baseline/").get_dataloader(batch_size=None, shuffle=False, num_workers=0)

Inspecting the networks
-----------------------

We can now iterate over the networks and print out the shape of each network:

.. code-block:: python

   print(f"Found {len(networks)} networks")

   # Checking shape of the networks
   for idx, (x,y) in enumerate(networks): 
       print("Network:", idx, x.shape, y.shape)