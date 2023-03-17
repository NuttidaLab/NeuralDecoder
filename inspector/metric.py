import numpy as np

class Metric:
    '''Base class for all RSA metrics'''

    def __init__(self):
        self.data = {}
        self.digested_data = {}
    
    def ingest(self, X, y, **kwargs):
        
        self.data['X'] = X
        self.data['y'] = y
        self.data['kwargs'] = kwargs

    def digest(self):
        pass

    def score(self):
        pass

    def plot(self):
        pass

    def report(self):
        '''Report the the metric's parameters and results statistics'''

        pass