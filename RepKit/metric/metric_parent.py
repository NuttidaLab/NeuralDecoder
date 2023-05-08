
from matplotlib import pyplot as plt
import seaborn as sns

class RepKitMetric:
    
    distances = None
    metric_name = None
    
    def __init__(self) -> None:
        pass

    def measure(self, data, metric):
        raise NotImplementedError()
    
    def plot(self, title = None):
        ax = sns.heatmap(self.distances, 
                         cmap='Blues_r', 
                         annot=False, 
                         fmt=".2f", 
                         square=True, 
                         cbar=True, 
                         cbar_kws={"shrink": .8})

        if title is None: title = self.metric_name
        ax.set_title(title)

        for _, spine in ax.spines.items():
            spine.set_visible(True)
        
        plt.plot()