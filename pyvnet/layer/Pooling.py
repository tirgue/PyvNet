import numpy as np

class Pooling():
    def __init__(self, size):
        self.size = size

    def reduce(self, np_image):
        s1 = int(np.ceil(np_image.shape[0] / self. size))
        s2 = int(np.ceil(np_image.shape[1] / self. size))
        np_output = np.zeros((s1, s2))
        for i in range(s1):
            for j in range(s2):
                image_slice = np_image[i*self.size:i*self.size+self.size, j*self.size:j*self.size+self.size]
                np_output[i, j] = np.max(image_slice)

        return np_output

if __name__ == "__main__":
    np.random.seed(10)
    image = np.random.randint(-100, 100, (7,7))
    print(image)
    pooling = Pooling(5)
    print(pooling.reduce(image))
