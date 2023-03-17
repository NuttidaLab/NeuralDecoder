"""The inspector package provides utilities for testing deep learning models' latent representations using various Representational Similarity Analysis (RSA) techniques.

This package includes functions for performing various RSA techniques such as:

- NetRep
- Multi-Dimensional Scaling (MDS)
- Hierarchical Clustering
- and Principal Component Analysis (PCA)

These techniques can be used to measure and visualize the similarity structure of the representations in a lower-dimensional space and identify clusters or patterns in the data.
"""

from .metric import Metric