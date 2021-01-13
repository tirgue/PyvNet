from pyvnet.layer import LayerBuilder

PYVNET_PARAM = {
    'architecture' : [
        {
            'type' : 'Convolutionnal',
            'size' : 5,
            'min' : -1,
            'max' : 1,
        }, 
        {
            'type' : 'Pooling',
            'size' : '5',
        },
        {
            'type' : 'Activation',
            'function' : 'Relu',
        },
        {
            'type' : 'NeuralNetwork',
            'hidden_layers_size' : [6, 3],
            'output_size' : 1
        }
    ]
}

class PyvNet():
    def __init__(self, params):
        self.layers = []
        for layer in params.get('architecture'):
            self.layers.append(LayerBuilder.build(layer))