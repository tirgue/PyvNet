import numpy as np

class Activation():

    @staticmethod
    def Relu(np_image):
        return np.maximum(0, np_image)

    @staticmethod 
    def Sigmoid(np_image):
        return 1 / (1 + np.exp(- np_image))

if __name__ == "__main__":
    np.random.seed(10)
    image = np.random.randint(-10,10,(10,10))
    print(image)
    print(Activation.Relu(image))
    print(Activation.Sigmoid(image))