.. You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to RepKit's documentation!
==================================

.. toctree::
   :maxdepth: 10
   :caption: Tutorials:

   1_inst
   2_basic
   3_ds_dl
   4_met
   5_spaces

.. autosummary::
   :toctree: _autosummary
   :recursive:
   :caption: API Reference:

   RepKit



Supported Metrics:
========================

=========================  ========================
model_metrics              
=========================  ========================
Metric                     Map
-------------------------  ------------------------
braycurtis                 modelwise_classical
canberra                   modelwise_classical
chebyshev                  modelwise_classical
cityblock                  modelwise_classical
correlation                modelwise_classical
cosine                     modelwise_classical
dice                       modelwise_classical
euclidean                  modelwise_classical
hamming                    modelwise_classical
jaccard                    modelwise_classical
jensenshannon              modelwise_classical
kulczynski1                modelwise_classical
mahalanobis                modelwise_classical
matching                   modelwise_classical
minkowski                  modelwise_classical
rogerstanimoto             modelwise_classical
russellrao                 modelwise_classical
seuclidean                 modelwise_classical
sokalmichener              modelwise_classical
sokalsneath                modelwise_classical
sqeuclidean                modelwise_classical
yule                       modelwise_classical
esm                        netrep_esm
gsm                        netrep_gsm
=========================  ========================

=========================  ========================
sample_metrics              
=========================  ========================
Metric                     Map
-------------------------  ------------------------
braycurtis                 samplewise_classical
canberra                   samplewise_classical
chebyshev                  samplewise_classical
cityblock                  samplewise_classical
correlation                samplewise_classical
cosine                     samplewise_classical
dice                       samplewise_classical
euclidean                  samplewise_classical
hamming                    samplewise_classical
jaccard                    samplewise_classical
jensenshannon              samplewise_classical
kulczynski1                samplewise_classical
mahalanobis                samplewise_classical
matching                   samplewise_classical
minkowski                  samplewise_classical
rogerstanimoto             samplewise_classical
russellrao                 samplewise_classical
seuclidean                 samplewise_classical
sokalmichener              samplewise_classical
sokalsneath                samplewise_classical
sqeuclidean                samplewise_classical
yule                       samplewise_classical
=========================  ========================

Note:
-----
-The modelwise_classical metrics are the same as the samplewise_classical metrics but averaged over samples.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
