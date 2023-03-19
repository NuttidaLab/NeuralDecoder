# 📝Notebooks

This folder contains Jupyter notebooks for experimentation and study purposes. It helps to keep the project organized by separating experimental work from other important components. Users can refer to the notebooks to gain insights into the project's development and see how ideas were tested and refined. However, caution should be exercised as the notebooks may contain errors or unfinished work. The folder serves as a valuable resource for anyone interested in the project's development and thought process.

## Logs

| name                              | source                                                            | status | notes                                                                                 |
| --------------------------------- | ----------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------- |
| netrep_workflow                   | self                                                              | ✅     | All ready to go! :D                                                                   |
| netrep_linear_metrics             | [NetRep Repo](https://github.com/ahwillia/netrep/tree/main/examples) | ✅     | probably not so relevant to the project                                               |
| netrep_stochastic_metrics         | [NetRep Repo](https://github.com/ahwillia/netrep/tree/main/examples) | ✅     | explored - GaussianStochasticMetric and EnergyStochasticMetric                      |
| baseline_flattened_representation | self                                                              | ✅     | Killed by Out Of Memory Killer on Monkee + Laptop. Improvements to core NetRep needed |
| baseline_esm_per_time_step        | self                                                              | ✅     | Laptop = dead 😵                                                                      |
| baseline_esm_per_time_step_v2     | self                                                              | ✅     | Improved; Running 20 frames 10 models (~1hr job) on Monkee                            |
| baseline_flattened_downsampled    | self                                                              | 🚧     | ~50 frames evenly split                                                               |
|                                   |                                                                   |        |                                                                                       |

## Things to investigate

| type             | name                                 | status |
| ---------------- | ------------------------------------ | ------ |
| General          | NetRep - EnergyStochasticMetric      | ✅     |
| General          | NetRep - GaussianStochasticMetric    | 🚧     |
| General          | Wasserstein Distance                 | 🚧     |
| General          | Canonical Correlation Analysis (CCA) | 🚧     |
| General          | Multi-Dimensional Scaling (MDS)      | 🚧     |
| General          | Dynamic Time Warping (DTW)           | 🚧     |
| General          | Frechet Distance                     | 🚧     |
| Gradient-based   | Saliency maps                        | 🚧     |
| Gradient-based   | Integrated Gradients                 | 🚧     |
| Activation-based | Activation maximization              | 🚧     |
| Activation-based | T-SNE visualization                  | 🚧     |
| Network pruning  | Weight pruning                       | 🚧     |
| Network pruning  | Structured pruning                   | 🚧     |
