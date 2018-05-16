from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from matplotlib import pyplot as plt
import numpy as np
from keras.datasets import mnist
#mnist = np.load("mnist_local.npz")


#print(globals())
#By hardcoding the psuedrandom number generator, we can reproduce the results.
np.random.seed(123)

#Load pre-shuffled MNIST dat into train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#print (x_train.shape)
plt.imshow(x_train[0])
