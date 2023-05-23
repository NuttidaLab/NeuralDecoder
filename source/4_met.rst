4: Metrics
==========

Understanding Metrics
----------------------

Metrics are the way to measure the (dis)similarity between two modles, classes, or samples. There are various metrics that have been implemented for representational similarity analysis. The growing list of supported metrics are:

=========================  ========================================= 
Metric                     Map                     
=========================  ========================================= 
braycurtis                 modelwise_classical, samplewise_classical
canberra                   modelwise_classical, samplewise_classical
chebyshev                  modelwise_classical, samplewise_classical
cityblock                  modelwise_classical, samplewise_classical
correlation                modelwise_classical, samplewise_classical
cosine                     modelwise_classical, samplewise_classical
dice                       modelwise_classical, samplewise_classical
euclidean                  modelwise_classical, samplewise_classical
hamming                    modelwise_classical, samplewise_classical
jaccard                    modelwise_classical, samplewise_classical
jensenshannon              modelwise_classical, samplewise_classical
kulczynski1                modelwise_classical, samplewise_classical
mahalanobis                modelwise_classical, samplewise_classical
matching                   modelwise_classical, samplewise_classical
minkowski                  modelwise_classical, samplewise_classical
rogerstanimoto             modelwise_classical, samplewise_classical
russellrao                 modelwise_classical, samplewise_classical
seuclidean                 modelwise_classical, samplewise_classical
sokalmichener              modelwise_classical, samplewise_classical
sokalsneath                modelwise_classical, samplewise_classical
sqeuclidean                modelwise_classical, samplewise_classical
yule                       modelwise_classical, samplewise_classical
esm                        netrep_esm
gsm                        netrep_gsm
=========================  =========================================

`Notice:`

- The modelwise_classical metrics are the same as the samplewise_classical metrics but averaged over samples.
- The :code:`netrep_esm` and :code:`netrep_gsm` metrics are only available for modelwise measurements.


Metrics and Shapes
------------------

Metric implementations are specific to spaces. Only certain metrics are available in certain spaces. The above table shows the mapping of the metric to the respective space.

Similarly, metrics are also restricted to work only on shapes recognized by the spaces. 

`reminder: the shapes are:`

========== ==========
Space      Shape
========== ==========
model      `(n_model, n_samples, n_features)`
class      `(n_class, n_samples, n_features)`
sample     `(n_samples, n_features)`
========== ==========

For example, the :code:`euclidean` metric is available in the :code:`modelwise_classical` and :code:`samplewise_classical` spaces and can accept both `(n_samples, n_features)` and `(n_model, n_samples, n_features)`. However, The :code:`netrep_esm` and :code:`netrep_gsm` metrics are only available in the :code:`modelwise_classical` space and can only accept `(n_model, n_samples, n_features)` shape.


Making our own Metrics
----------------------



Template 1: Simple pairwise metric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import numpy as np
    import itertools
    from tqdm import tqdm

    class custom_metric_example:
        def __init__(self) -> None:
            pass

        def measure(self, data):

            n_data = len(data)

            distances = np.zeros((n_data, n_data))

            for i,j in tqdm(itertools.combinations(range(n_data), 2), total = n_data * (n_data - 1) / 2):
                x1, y1 = data[i]
                x2, y2 = data[j]
                # For example, this just subtracts the samples
                distances[i, j] = x1 - x2
                
            distances += distances.T
            
            # return the distance matrix
            return distances

Notes to remember
-----------------

- The :code:`measure` function takes in a list of data and returns a distance matrix. And it is a mandatory function.
- The :code:`__init__` function is optional. It can be used to initialize any variables that are required for the metric.
- The :code:`measure` function returns a square distance matrix of shape (n_data, n_data). The diagonal elements are ignored/ assumed 0. The upper triangular elements are used to fill the lower triangular elements. The distance matrix is symmetric.