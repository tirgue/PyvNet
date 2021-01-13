import numpy as np

class Convolutionnal():
    def __init__(self, size, min = -1, max = 1):
        if size != None and min != None and max != None:
            self.size = size
            self.min = min
            self.max = max
            self.np_filter = np.random.rand(self.size, self.size) * (self.max - self.min) + self.min

    def filter(self, np_image):
        biais = int(self.size / 2)
        f1 = np_image.shape[0] - self.size
        f2 = np_image.shape[1] - self.size
        np_output = np.zeros((f1+1, f2+1))
        for i in range(0, f1+1):
            for j in range(0, f2+1):
                image_slice = np_image[i:i+self.size, j:j+self.size]
                np_output[i, j] = np.sum(image_slice * self.np_filter)

        return np_output

if __name__ == "__main__":
    np.random.seed(10)
    conv = Convolutionnal(3)
    print(conv.np_filter)
    image = np.random.randint(0, 2, (4,4))
    print(image)

    output = conv.filter(image)
    print(output)