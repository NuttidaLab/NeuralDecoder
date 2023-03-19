import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distmat(distmat, title = "Distance Metric", size = 8):
    '''Plot a distance matrix
    New method uses Seaborn to create a heatmap
    '''

    # Set the x and y ticks to the labels
    number_of_networks = len(distmat[0])
    labels = [f"Network {i+1}" for i in range(number_of_networks)]

    # Create a figure and set the size
    fig, ax = plt.subplots(figsize=(size, size))

    # Plot the heatmap using Seaborn
    sns.heatmap(distmat, cmap='coolwarm', annot=True, fmt=".3f",
                xticklabels=labels, yticklabels=labels, cbar_kws={'label': 'Distance'})

    # Set the title and axis labels
    ax.set(title=title)

    # Show the plot
    plt.show()


def plot_distmat_old(distmat, title = "Distance Metric", size = 5):
    '''Plot a distance matrix
    Uses only matplotlib, felt like it did not look as good and hard to control
    '''

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
