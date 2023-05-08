Tutorial: Measuring Model Similarity and Visualizing Model Space with RepKit
============================================================================

In this tutorial, we will demonstrate how to use RepKit to measure the similarity between a set of networks and visualize their model space. We will use the `model_space` module from the `RepKit.space` package to measure the pairwise cosine similarity between the networks and visualize their 2D embedding using multidimensional scaling.

Before we get started, make sure you have RepKit installed. You can install it using pip:

.. code-block:: bash

   pip install RepKit

Importing the necessary modules
-------------------------------

First, we need to import the necessary modules. In this case, we need to import the `model_space` module from `RepKit.space`:

.. code-block:: python

   from RepKit.space import model_space

Loading the networks
---------------------

Before we can measure the similarity between the networks, we need to load them as a PyTorch DataLoader object. We can do this using the `rnn.flow()` function from the `RepKit.dataset` package, as we did in the previous tutorial:

.. code-block:: python

   from RepKit.dataset import rnn

   networks = rnn.flow("data/baseline/").get_dataloader(batch_size=None, shuffle=False, num_workers=0)

Measuring the similarity and visualizing the model space
--------------------------------------------------------

Next, we can use the `model_space` module to measure the pairwise cosine similarity between the networks, and then visualize their 2D embedding using multidimensional scaling:

.. code-block:: python

   space = model_space()

   # Measure pairwise cosine similarity
   space.measure(networks, "cosine")

   # Plot the distance matrix
   space.plot_distance()

   # Compute the 2D embedding using multidimensional scaling
   space.decompose(components=2, engine="mds")

   # Plot the 2D embedding with labels
   space.plot_embedding(labels=[1, 5, 10, 0])
