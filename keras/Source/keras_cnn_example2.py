from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from matplotlib import pyplot as plt
import numpy as np
import subprocess as sub
from keras.datasets import mnist
#import StartIdle as si

#By hardcoding the psuedrandom number generator, we can reproduce the results.
np.random.seed(123)

def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #sub.call('python -m idlelib.idle')
    print('shape 1: {0}'.format(x_train.shape))
    plt.imshow(x_train[0])

    x_train = x_train.reshape(x_train.shape[0],1, 28, 28)
    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28)

    print('shape 2: {0}'.format(x_train.shape))

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    print(y_train.shape)
    print(y_train[:10])

    # Convert 1-dimensional class arrays to 10-dimensional class matrices
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    
    print(y_train.shape)
    print('\n')
    

    ####----####
    model = Sequential()
    model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1, 28, 28)))

    print(model.output_shape)


    model.add(Convolution2D(32, 3, 3, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

    model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=10, verbose=1)

    score = model.evaluate(X_test, Y_test, verbose=0)

    print(score)

if __name__ == '__main__':
    main()
