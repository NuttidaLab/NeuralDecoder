import numpy as np
import matplotlib.pyplot as plt

def plot_distmat(distmat, title = "Distance Metric", size = 5):
    '''Plot a distance matrix'''

    # Create a figure and a 3D Axes
    fig, ax = plt.subplots(1, 1, figsize=(size, size))
    im = ax.imshow(distmat)

    # Set the x and y ticks to the labels
    number_of_networks = len(distmat[0])

    labels = [f"Network {i+1}" for i in range(number_of_networks)]

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
            
            # set text size to fit in the box dynamically
            text.set_size(1.0 / (number_of_networks * 0.5) * 12)
    
    ax.set(title=title)
    plt.colorbar(im)
    plt.show()