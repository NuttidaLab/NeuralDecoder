import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap

def export_distmat(distmat, out_dir, title, normalize = True, annot = True, format = "eps", color_map_hex = []):
    """ Export a distance matrix to a file
    """

    if normalize:
        distmat = [result / np.max(result) for result in distmat]

    if color_map_hex:
        boundaries = [0.0, 1.0]
        hex_colors = color_map_hex
        colors=list(zip(boundaries, hex_colors))
        custom_color_map = LinearSegmentedColormap.from_list(
            name='custom_navy',
            colors=colors,
        )
        cmap = custom_color_map
    else:
        cmap = 'coolwarm'

    fig = plt.figure()
    ax = sns.heatmap(distmat, cmap=cmap, annot=annot, fmt=".2f")
    ax.set_title(title)

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    location = os.path.join(os.path.abspath(out_dir), f'{title}.{format}')

    plt.savefig(location, format=format)

# def export_distmat(distmat, out_dir, title, annot = True, format = "eps", color_map_hex = 'coolwarm'):
#     """ Export a distance matrix to a file
#     """
#     fig = plt.figure()
#     ax = sns.heatmap(distmat, cmap=color_map_hex, annot=annot, fmt=".2f")
#     ax.set_title(title)

#     Path(out_dir).mkdir(parents=True, exist_ok=True)
#     location = os.path.join(os.path.abspath(out_dir), f'{title}.{format}')

#     plt.savefig(location, format=format)

def plot_distmat(distmat, title = "Distance Metric", out_path = None):
    """Plot a distance matrix
    New method uses Seaborn to create a heatmap
    """

    # Set the x and y ticks to the labels
    number_of_networks = len(distmat[0])
    labels = [f"Network {i+1}" for i in range(number_of_networks)]

    # Create a new figure
    plt.figure()

    # Plot the heatmap using Seaborn
    ax = sns.heatmap(distmat, cmap='coolwarm', annot=True, fmt=".3f",
                     xticklabels=labels, yticklabels=labels, cbar_kws={'label': 'Distance'})
    ax.set_title(title)

    # if out_path is not None, save the figure to the path
    if out_path is not None:
        ax.figure.savefig(out_path, bbox_inches='tight')
    else:
        plt.show()


def plot_distmat_old(distmat, title = "Distance Metric", size = 5):
    """Plot a distance matrix
    Uses only matplotlib, felt like it did not look as good and hard to control
    """

    # Create a figure and a 3D Axes
    fig, ax = plt.subplots(1, 1, figsize=(size, size))
    im = ax.imshow(distmat)

    # Set the x and y ticks to the labels
    number_of_networks = len(distmat[0])

    # Create a list of labels for the x and y ticks
    labels = [f"Network {i+1}" for i in range(number_of_networks)]

    # Set the x and y ticks to the labels
    ax.set_xticks(np.arange(number_of_networks))
    ax.set_yticks(np.arange(number_of_networks))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    # rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")
    
    # Loop over data dimensions and create text annotations.
    for i in range(number_of_networks):
        for j in range(number_of_networks):

            # Show only 3 decimal places
            text = ax.text(j, i, f"{distmat[i, j]:.3f}", ha="center", va="center", color="w")
            
            # Set text size to be 80% of the cell size
            text.set_fontsize(0.8 * size * 100 / number_of_networks)
            
    ax.set(title=title)
    plt.colorbar(im)
    plt.show()
