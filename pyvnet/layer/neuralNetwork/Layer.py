import numpy as np

class Layer():
    def __init__(self, size):
        self.size = size
        self.weights = None
        self.initializeBiais()
        self.previousLayer = None
        self.nextLayer = None
        self.values = np.zeros(size)

    def initializeWeights(self):
        self.weights = np.random.rand(self.previousLayer.size, self.size) * 2 - 1

    def initializeBiais(self):
        self.biais = np.random.rand(self.size) * 2 -1

    def computeValues(self):
        self.values = np.dot(self.previousLayer.values, self.weights) + self.biais