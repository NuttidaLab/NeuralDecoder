2: Basic Usage and API
======================

In this tutorial, we will demonstrate how to use RepKit to load and inspect a set of networks. We will use the RepKit :code:`rnn` module to load a set of networks from a directory, and then inspect the shape of each network in the set.

Once we explore the loading and unloading of the data, we will then explore how to measure the similarity between two networks and plot them in a low-dimensional space.

For this, We will use the :code:`model_space` module from the :code:`RepKit.space` package to measure the pairwise cosine similarity between the networks and visualize their 2D embedding using multidimensional scaling.

Understanding RepKitDataset
---------------------------

All datasets used in RepKit are a child of the :code:`RepKitDatasetClass` which inturn is a child of :code:`torch.utils.data.Dataset`.


Importing the necessary modules
-------------------------------

First, we need to import the necessary modules. In this case, we only need to import the :code:`rnn` module which is one of various pre-defined datasets from :code:`RepKit.dataset`:

.. code-block:: python

   from RepKit.dataset import rnn
   from RepKit.space import model_space

Loading the networks
---------------------

Next, we can load the networks using the :code:`rnn.flow()` function and create a PyTorch DataLoader object for the networks using the :code:`get_dataloader()` function:

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

Measuring the Cosine similarity
-------------------------------

Next, we can use the :code:`model_space` module to measure the pairwise cosine similarity between the networks, and then visualize their 2D embedding using multidimensional scaling:

.. code-block:: python

   space = model_space()

   # Measure pairwise cosine similarity
   space.measure(networks, "cosine")

   # Plot the distance matrix
   space.plot_distance()


Decomposing and visualizing 2D embedding
----------------------------------------

Finally, we can decompose the distance matrix into a 2D embedding using multidimensional scaling and plot the 2D embedding with labels:

.. code-block:: python

   # Compute the 2D embedding using multidimensional scaling
   space.decompose(components=2, engine="mds")

   # Plot the 2D embedding with labels
   space.plot_embedding(labels=[1, 5, 10, 0])


Notes:
------
- You can use any one of the supported metric (instead of cosine) to measure the similarity matrix. The supported metrics are can be found in :code:`space.metric.registered_metrics`. Similarly, you can use any of the supported decomposers while generating the embeddings.
- As you are playing with the space object that keeps track of state changes, you can chain multiple functions together. For example, in a single line of code: :code:`space.measure(networks, cosine").plot_distance().decompose(components=2, engine="mds").plot_embedding(labels=[1, 5, 10, 0])`
- Furthermore, you can also pass in your custom metric or decomposer to the :code:`measure()` and :code:`decompose()` functions respectively. For more information, please refer to the :code:`RepKit.space` module or tutorial 5.