from .metric_parent import RepKitMetric
from .model.classical import Classical as modelwise_classical
# from .model.classical import Netrep as modelwise_netrep

class model_metric(RepKitMetric):
    """A class to measure model-based metrics for representation learning.

    Attributes:
        registered_metrics (list): A list of classes that implement model-based metrics.
        all_supported (list): A list of all supported metric names.
    """

    registered_metrics = [modelwise_classical]
    all_supported = []

    def __init__(self) -> None:
        """Initializes the model_metric class.

        Populates the all_supported list with the supported metric names from the registered_metrics classes.
        Calls the parent class constructor.
        """
        
        for sup in self.registered_metrics: self.all_supported += sup.supported
        super().__init__()

    def measure(self, data, metric):
        """Measures a model-based metric for a given data.

        Args:
            data: The data to be evaluated. The format `models x samples x features`.
            metric (str): The name of the metric to be measured.

        Returns:
            A numpy array of distances or scores according to the metric.

        Raises:
            ValueError: If the metric is not supported.
        """

        self._ensure_supported(metric)
        # for now only classical
        self.metric_name = metric
        self.distances = modelwise_classical().measure(data, metric)
        return self.distances

    def _ensure_supported(self, metric):
        """Checks if a metric is supported by the class.

        Args:
            metric (str): The name of the metric to be checked.

        Raises:
            ValueError: If the metric is not supported.
        """

        if metric not in self.all_supported: raise ValueError(f"Unsupported metric: {metric}")