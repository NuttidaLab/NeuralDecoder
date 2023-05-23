3: Datasets And DataLoaders
===========================

Now that we have seen how to load a dataset, we can make our own dataset. In this example, we will make a dataset that loads networks from a directory and then slices the data.

Making our own dataset
-----------------------

.. code-block:: python

   class samples(RepKitDataset):
      def __init__(self, file_path: str, preprocess: str = None) -> None:

         self.data = None
         self.labels = None

         data = io.loadmat(file_path)
         
         ltm = data["all_ltm_spks"]
         tst = data["all_tst_spks"]
         wm = data["all_wm_spks"]

         ltm = self.slice_data(ltm, 2500)
         tst = self.slice_data(tst, 2000)
         wm = self.slice_data(wm, 2500)

         self.data = np.array([ltm, tst, wm]).transpose(1,0,2)
   
      def slice_data(self, arr, min_len):
         t = []
         for i in range(60):
               t.append(arr[i][:min_len])
         return np.array(t)
      
      def __len__(self):
         return len(self.data)

      def __getitem__(self, idx):
         return self.data[idx], self.labels[idx] if self.labels is not None else None


Notice how the `__getitem__` and `__len__` remain consitant. This is a requirement for all datasets.

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

- The `__getitem__` and `__len__` methods are required for all datasets.
- The `__getitem__` method must return a tuple of the data and the label.
- The `__len__` method must return the length of the dataset.
- The `__init__` method must set the data and labels to None (if not used).
