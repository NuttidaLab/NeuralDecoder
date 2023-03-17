# 🔎RSA Investigations: Decoding Representations in Deep Learning Models

This repository contains the code and data for the research of comparing various RSA techniques to interpret and quantify representations

> **Abstract:** This research aims to investigate the efficacy of representational similarity analysis (RSA) techniques in characterizing the latent semantic features of deep learning models. Specifically, we evaluate the semantic representations of our biophysically realistic deep learning models that are trained to perform cognitive tasks, such as working memory retention. We explore the sensitivity of these RSA techniques to various noise setups, including different levels of internal noise, external/input noise, and network parameter initialization. Our results demonstrate the usefulness of these RSA measures in quantifying the similarity and dissimilarity of neural representations across different physiologically constrained models, providing important insights into the underlying cognitive processes involved in these tasks. This research contributes to the growing interest in understanding the neural representations of deep learning models and their potential applications in neuroscience.

## Repository Structure

The `notebooks` folder in the repository contains Jupyter notebooks for experimentation and study purposes. It helps to keep the project organized by separating experimental work from other important components. Users can refer to the notebooks to gain insights into the project's development and see how ideas were tested and refined. However, caution should be exercised as the notebooks may contain errors or unfinished work. The folder serves as a valuable resource for anyone interested in the project's development and thought process.

More, TBD...

## Requirements and Usage

To run this code, you will need:

- `Python 3.7` or higher
- `cuda` installed

You can install these dependencies using `pip install -r requirements.txt`.

## Current status

This section provides an overview of the current state of the project. It may include information on ongoing work, upcoming features, or bug fixes.

### RSA Implementations

It organizes what different RSA implementations are available in the codebase and which ones are actively being developed or maintained.

| Name   | Source                                    | Resource                                                                                       | Status                                  |
| ------ | ----------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| NetRep | [GitHub](https://github.com/ahwillia/netrep) | [Paper 1](https://arxiv.org/pdf/2110.14739.pdf)<br />[Paper 2](https://arxiv.org/pdf/2211.11665.pdf) | [🚧](https://emojipedia.org/construction/) |
|        |                                           |                                                                                                |                                         |

### Noise Setups

For understanding how noise is being modeled in the code and which setups are being used for the project's experiments.

| Identifier | Description | Approximation | Status |
| ---------- | ----------- | ------------- | ------ |
| TBD        | TBD         | TBD           | TBD    |
|            |             |               |        |

## Results

For help with understanding what conclusions have been drawn from the experiments and what the next steps in the project may be.

| RSA | Noise | Notes |
| --- | ----- | ----- |
| TBD | TBD   | TBD   |
|     |       |       |

## Citation

If you use this code or data for your own research, please cite our paper as follows:

```BibTeX
@inproceedings{nuttidalabs2023,
  title={Unpacking the Latent Semantic Features of Neuromorphic RNNs: An RSA Analysis},
  author={Singha, Rudramani and Rungratsameetaweemana, Nuttida},
  booktitle={Proceedings of the NuttidaLabs Conference on Artificial Intelligence and Neuroscience},
  year={2023}
}
```
