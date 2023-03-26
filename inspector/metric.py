import numpy as np

class Metric:
    """Base class for all RSA metrics"""

    def __init__(self, verbose=True):
        self.data = {}
        self.verbose = verbose
    
    def ingest(self, X, y, preprcessed = False):
        
        self.data['X'] = X
        self.data['y'] = y
        self.data['digested_flag'] = False

        if preprcessed:
            self.data['digested_networks'] = X
            self.data['digested_flag'] = True

        return "TBD ingestion report"

    def digest(self):
        pass

    def score(self):
        pass

    def plot(self):
        pass

    def report(self):
        """Report the the metric's parameters and results statistics"""
        pass