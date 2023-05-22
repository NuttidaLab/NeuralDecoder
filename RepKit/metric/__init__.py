from .metric_parent import RepKitMetric
from .model.classical import Classical as modelwise_classical
from .model.netrep import ESM as netrep_esm
from .model.netrep import GSM as netrep_gsm

METRIC_MAP = {
    "model_metric": {
        "braycurtis": "modelwise_classical",
        "canberra": "modelwise_classical",
        "chebyshev": "modelwise_classical",
        "cityblock": "modelwise_classical",
        "correlation": "modelwise_classical",
        "cosine": "modelwise_classical",
        "dice": "modelwise_classical",
        "euclidean": "modelwise_classical",
        "hamming": "modelwise_classical",
        "jaccard": "modelwise_classical",
        "jensenshannon": "modelwise_classical",
        "kulczynski1": "modelwise_classical",
        "mahalanobis": "modelwise_classical",
        "matching": "modelwise_classical",
        "minkowski": "modelwise_classical",
        "rogerstanimoto": "modelwise_classical",
        "russellrao": "modelwise_classical",
        "seuclidean": "modelwise_classical",
        "sokalmichener": "modelwise_classical",
        "sokalsneath": "modelwise_classical",
        "sqeuclidean": "modelwise_classical",
        "yule": "modelwise_classical",
        "esm": "netrep_esm",
        "gsm": "netrep_gsm",
    }
}

class model_metric(RepKitMetric):
    """A class to measure model-based metrics for representation learning.

    Attributes:
        registered_metrics (list): A list of classes that implement model-based metrics.
        all_supported (list): A list of all supported metric names.
    """

    registered_metrics = METRIC_MAP["model_metric"]

    def __init__(self) -> None:
        """Initializes the model_metric class.

        Populates the all_supported list with the supported metric names from the registered_metrics classes.
        Calls the parent class constructor.
        """

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

        self.metric_name = metric

        mapped_class = self._ensure_supported(metric)

        if mapped_class == "modelwise_classical":
            self.distances = modelwise_classical().measure(data, metric)
        elif mapped_class == "netrep_esm":
            self.distances = netrep_esm().measure(data, metric)
        elif mapped_class == "netrep_gsm":
            self.distances = netrep_gsm().measure(data, metric)

        return self.distances

    def _ensure_supported(self, metric):
        """Checks if a metric is supported by the class.

        Args:
            metric (str): The name of the metric to be checked.

        Raises:
            ValueError: If the metric is not supported.
        """

        if metric not in self.registered_metrics.keys(): raise ValueError(f"Unsupported metric: {metric}")
        else: return self.registered_metrics[metric]