
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
                         cbar_kws={"shrink": 1})

        if title is None: title = self.metric_name
        ax.set_title(title)

        for _, spine in ax.spines.items():
            spine.set_visible(True)
        
        plt.plot()

    def ensure_supported(self, metric):
        """Checks if a metric is supported by the class.

        Args:
            metric (str): The name of the metric to be checked.

        Raises:
            ValueError: If the metric is not supported.
        """

        if metric not in self.registered_metrics.keys(): raise ValueError(f"REPKIT ERROR: Unsupported metric: {metric}")
        else: return self.registered_metrics[metric]