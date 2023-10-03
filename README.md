# 🧠RepKit: Representational Analysis Toolkit

[![Documentation](https://img.shields.io/badge/api-documentation-blue.svg)](https://nuttidalab.github.io/NeuralDecoder/) ![Documentation](https://img.shields.io/badge/python-3.11-blue.svg) [![CodeFactor](https://www.codefactor.io/repository/github/nuttidalab/neuraldecoder/badge)](https://www.codefactor.io/repository/github/nuttidalab/neuraldecoder)

This repository contains a collection of tools to measure, visualize, and, analyze representational similarities and latent semantic features. The tools are designed to be modular and flexible, allowing for easy integration into existing research/projects.

## Installation

```bash
git clone https://github.com/NuttidaLab/NeuralDecoder.git
cd RepKit
python setup.py install
```

## Toolkit Skeleton

* RepKit.dataset: Loads and processes the data. Has helpful predefined templates.
* RepKit.space: Manipulates the dataset. Supports Model and Sample spaces.
  * RepKit.space.measure: Contains a collection of measures - `space.metric.registered_metrics`
  * RepKit.space.decompose: Reduces the dimensionality and visualizes the spaces.

## Simple Example

```python
# Making x (200 samples, 300 features) and y (200 labels)
import numpy as np
x = np.random.rand(200, 300)
y = np.random.randint(2, size=200)

# The rnn package has got useful functions (one of which is register)
from RepKit.dataset.rnn import register
dataset = register(x, y)

# As our data is in sample space, we will import sample_space to manipulate it
from RepKit.space import sample_space
space = sample_space()

# We can then measure and reduce its dimensionality
space.measure(dataset, "cosine").plot_distance()
space.decompose(components=2, engine="mds").plot_embedding(labels=y)
```

## Citation

If you use this code or data for your own research, please cite our paper as follows:

```BibTeX
@inproceedings{nuttidalabs2023,
  title={Unpacking the Latent Semantic Features of Neuromorphic RNNs: An RSA Analysis},
  author={Singha, Rudramani and Rungratsameetaweemana, Nuttida},
  booktitle={Proceedings of the XYZ Conference on Artificial Intelligence and Neuroscience},
  year={2023}
}
```
