class RepKitDecomposer:
    engine = None
    embedding = None
    metric = None

    def __init__(self):
        pass
    
    def __str__(self):
        return self.embedding

    def decompose(self, distances, components):
        raise NotImplementedError()
    
    def plot(self):
        raise NotImplementedError()