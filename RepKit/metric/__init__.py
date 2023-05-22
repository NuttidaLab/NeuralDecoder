from .metric_parent import RepKitMetric

# Modelwise Imports
from .model.classical import Classical as modelwise_classical
from .model.netrep import ESM as netrep_esm
from .model.netrep import GSM as netrep_gsm

# Samplewise Imports
from .sample.classical import Classical as samplewise_classical

# Mapping
from .metric_map import METRIC_MAP

class model_metric(RepKitMetric):
    """A class to measure model-based metrics for representation analysis.

    Attributes:
        registered_metrics (list): A list of classes that implement model-based metrics.
        all_supported (list): A list of all supported metric names.
    """

    def __init__(self) -> None:
        """Initializes the model_metric class.

        Populates the all_supported list with the supported metric names from the registered_metrics classes.
        Calls the parent class constructor.
        """
        self.registered_metrics = METRIC_MAP["model_metric"]
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

        mapped_class = self.ensure_supported(metric)

        if mapped_class == "modelwise_classical":
            self.distances = modelwise_classical().measure(data, metric)
        elif mapped_class == "netrep_esm":
            self.distances = netrep_esm().measure(data, metric)
        elif mapped_class == "netrep_gsm":
            self.distances = netrep_gsm().measure(data, metric)

        return self.distances
    
class sample_metric(RepKitMetric):
    """A class to measure sample-based metrics for representation analysis."""

    def __init__(self) -> None:
        self.registered_metrics = METRIC_MAP["sample_metric"]
        super().__init__()

    def measure(self, data, metric):
        """Measures a sample-based metric for a given data.

        Args:
            data: The data to be evaluated. The format `samples x features`.
            metric (str): The name of the metric to be measured.

        Returns:
            A numpy array of distances or scores according to the metric.

        Raises:
            ValueError: If the metric is not supported.
        """

        self.metric_name = metric

        mapped_class = self.ensure_supported(metric)

        if mapped_class == "samplewise_classical":
            self.distances = samplewise_classical().measure(data, metric)

        return self.distances




