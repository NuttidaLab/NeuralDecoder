3: Datasets And DataLoaders
===========================

Understanding Datasets
----------------------

Datasets are the core of RepKit. They are the objects that hold the data and labels. They are also the objects that are passed to the dataloaders, metrics, and spaces. 

Every Dataset in RepKit is a child of the :code:`RepKitDataset` class. This class is a child of the :code:`torch.utils.data.Dataset` class. This means that every dataset in RepKit is a PyTorch dataset. This allows us to use the PyTorch dataloaders to load our data and utilize multi-threading for big measurements.

Datasets are required to have two methods: :code:`__getitem__` and :code:`__len__`. The :code:`__getitem__` method is used to get a single sample from the dataset. The :code:`__len__` method is used to get the length of the dataset. The :code:`__getitem__` method must return a tuple of the data and the label. The :code:`__len__` method must return the length of the dataset. The :code:`__init__` method must set the data and labels to None (if not used).

Shape of the data
-----------------

The shape of the data is extremely important in order to use the correct measurements and decomposers in different spaces. The shape of the data must be, according to spaces:

========== ==========
Space      Shape
========== ==========
model      `(n_model, n_samples, n_features)`
class      `(n_class, n_samples, n_features)`
sample     `(n_samples, n_features)`
========== ==========

For example, if the data is (n_samples, n_features, n_time_steps) and you want to embed them in the sample_space, then the data can be averaged across the n_features or the n_time_steps axis (whichever captures the most value/information).

`Note:`

- In class_space, it is expected that the n_samples is a vstack of the samples in all the models (if you want to measure class similarity across multiple models). Alternatively, you can measure class difference in single model individually and then compare across models in a different space.



Making our own dataset
-----------------------

Now that we have seen how to use the pre-defined datasets, we can make our own dataset. In the following templates, we will define various types of datasets for different purposes.

Template 1: Simple dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^
In this example, we will make a dataset that takes in data and labels and returns them in the expected format.

.. code-block:: python

   from RepKit.dataset import RepKitDataset
   import numpy as np

   class custom_dataset_example(RepKitDataset):
      def __init__(self, data: np.ndarray, labels: np.ndarray = None):
         self.data = data
         self.labels = labels
         super().__init__()

      def __len__(self):
         return len(self.data)

      def __getitem__(self, idx):
         return self.data[idx], self.labels[idx] if self.labels is not None else None

`Notice:`

- how it initialized the parent class at the end of the :code:`__init__` method (it is not mandetory).
- Entire data is loaded in memory (not recommended for big datasets).

Template 2: Flow from directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, we will make a dataset that loads networks from a directory.

.. code-block:: python

   from scipy import io

   class custom_dataset_example(RepKitDataset):
      def __init__(self, data_dir: str, n_items: int = None) -> None:
         self.paths = self.crawl_dir(data_dir, n_items)
         super().__init__()

      def __len__(self):
         return len(self.paths)

      def __getitem__(self, idx):
         data = io.loadmat(self.paths[idx])
         x = data['x_data']
         y = data['y_data']
         return x, y

`Notice:`

- It also inherits all the parent class's methods like :code:`get_dataloader()` and :code:`crawl_dir()`.
- The :code:`crawl_dir()` method is used to crawl a directory and return a list of paths to the files in the directory which is inherited from parent class.
- The data is not loaded in memory, only the link to the data is stored (recommended for big datasets).


Manipulating our own dataset
----------------------------

Now that we have our own dataset, we can manipulate it in the same way we did before.
In addition, we can chain multiple datasets to create subsets of datasets. For example:

.. code-block:: python

   from RepKit.dataset import rnn
   dataset = samples("n1.mat", preprocess="slice")
   xt, _ = dataset[0]
   datas = rnn.register(xt, None)
   datas.data.shape

Here for example, we have sliced the data and then registered it to the rnn dataset. This allows us to use the rnn dataset's methods on our own data.

Notes to remember
-----------------

- The :code:`__getitem__` and :code:`__len__` methods are required for all datasets.
- The :code:`__getitem__` method must return a tuple of the data and the label.
- The :code:`__len__` method must return the length of the dataset.
- The :code:`__init__` method must set the data and labels to None (if not used).
