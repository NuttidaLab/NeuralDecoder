import numpy as np
import scipy.io
import os

class DataLoader:

    def __init__(self):
        pass
    
    # Crawl the data directory
    def flow_from_mat(self, data_dir, n_networks = 5, binarize_y = True, average_x = True):
        """Reads the data from the data directory and returns the data in the form of numpy arrays

        1. Averages all the neurons across the timestep dimentions
        2. Averages the last 50 timesteps of y
        3. Binarizes the y values
        """

        data_files = [os.path.join(os.path.abspath(data_dir), f) for f in os.listdir(data_dir) if f.endswith('.mat')]
        # loop over the files

        all_x = []
        all_y = []

        for i, f in enumerate(data_files[:n_networks]):
            data = scipy.io.loadmat(f)
            all_x.append(data['test_x'])
            all_y.append(data['test_out'])

        all_x = np.array(all_x)
        all_y = np.array(all_y)

        if binarize_y:
            all_y = all_y[:, :, :, -50:]
            all_y = np.average(all_y, axis=3)
            all_y = all_y.reshape(all_y.shape[0], -1)

            # for every value in all_y, if it is greater than 0, set it to 1, else set it to -1
            all_y[all_y > 0] = 1
            all_y[all_y < 0] = -1
        
        if average_x:
            all_x = np.average(all_x, axis=3)
            all_x = all_x.reshape(all_x.shape[0], all_x.shape[1]*all_x.shape[2], all_x.shape[3])

        return all_x, all_y

