from .Convolutionnal import Convolutionnal
from .Pooling import Pooling
from .Activation import Activation
from .neuralNetwork.NeuralNetwork import NeuralNetwork

class LayerBuilder():
    @staticmethod
    def build(layer):
        return {
            'Convolutionnal': Convolutionnal(layer.get('size'), layer.get('min'), layer.get('max')),
            'Pooling': Pooling(layer.get('size')),
            'Activation': getattr(Activation, str(layer.get('function'))) if (layer.get('function') != None) else None,
            'NeuralNetwork': NeuralNetwork(10, layer.get('output_size'), layer.get('hidden_layers_size')),
        }[layer.get('type')]
    
