# 🧠RepKit: Represntational Analysis Toolkit

[![Documentation](https://img.shields.io/badge/api-documentation-blue.svg)](https://nuttidalab.github.io/NeuralDecoder/) ![Documentation](https://img.shields.io/badge/python-3.6+-blue.svg) [![CodeFactor](https://www.codefactor.io/repository/github/nuttidalab/neuraldecoder/badge)](https://www.codefactor.io/repository/github/nuttidalab/neuraldecoder)

This repository contains a collection of tools to measure, visualize, and,simple code sample analyze representational similarities and latent semantic features. The tools are designed to be modular and flexible, allowing for easy integration into existing research/projects.

## Installation

```bash
git clone https://github.com/NuttidaLab/NeuralDecoder.git
cd RepKit
python setup.py install
```

## Toolkit Skeleton

* RepKit.dataset: Loads and processes the data. Has helpful predefined templates.
* RepKit.space: Manipulates the dataset. Supports Model and Sample spaces.
  * RepKit.space.measure: Contains a collection of measures to quantify the latent semantic features of a space.
  * RepKit.space.decompose: Reduces the dimensionality and visualizes the spaces.

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
