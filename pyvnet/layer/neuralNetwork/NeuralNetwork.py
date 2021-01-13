import numpy as np
from pyvnet.layer.neuralNetwork.Layer import Layer 

class NeuralNetwork():
    def __init__(self, input_size, output_size, hidden_layers_size):
        if input_size != None and output_size != None and hidden_layers_size != None:
            self.input_size = input_size
            self.output_size = output_size
            self.layers = [Layer(input_size)]
            for size in hidden_layers_size + [output_size]:
                layer = Layer(size)
                layer.previousLayer = self.layers[-1]
                self.layers[-1].nextLayer = layer
                layer.initializeWeights()
                self.layers.append(layer)

    def think(self, np_input):
        self.layers[0].values = np_input
        for i in range(1, len(self.layers)):
            self.layers[i].computeValues()

        return self.layers[-1].values
