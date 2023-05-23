.. You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to RepKit's documentation!
==================================

.. autosummary::
   :toctree: _autosummary
   :recursive:
   :caption: API Reference:

   RepKit


.. toctree::
   :maxdepth: 10
   :caption: Tutorials:

   1_inst
   2_basic
   3_ds_dl
   4_met
   5_spaces


Supported Metrics:
========================

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

Supported Decomposers:
========================
=========================  ========================================= 
Decomposer                 Map                  
=========================  ========================================= 
MDS                        `MDS <https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html>`_
PCA                        `PCA <https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html>`_
=========================  =========================================


Note:
-----
- The modelwise_classical metrics are the same as the samplewise_classical metrics but averaged over samples.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
