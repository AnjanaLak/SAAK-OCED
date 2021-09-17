from keras.layers import Activation
import keras
import numpy as np
import tensorflow
from keras import backend as K
from keras.layers import Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential


def getImageClass(image):
    tensorflow.compat.v1.disable_eager_execution()  # added by me
    K.clear_session()
    tensorflow.compat.v1.reset_default_graph()  # tf.compat.v1.reset_default_graph()

    img_width, img_height = 350, 350

    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    modelI = Sequential()
    modelI.add(Conv2D(32, (2, 2), input_shape=input_shape))
    modelI.add(Activation('relu'))
    modelI.add(MaxPooling2D(pool_size=(2, 2)))

    modelI.add(Conv2D(32, (2, 2)))
    modelI.add(Activation('relu'))
    modelI.add(MaxPooling2D(pool_size=(2, 2)))

    modelI.add(Conv2D(64, (2, 2)))
    modelI.add(Activation('relu'))
    modelI.add(MaxPooling2D(pool_size=(2, 2)))

    modelI.add(Flatten())
    modelI.add(Dense(64))
    modelI.add(Activation('relu'))
    modelI.add(Dropout(0.5))
    modelI.add(Dense(2))
    modelI.add(Activation('softmax'))

    modelI.compile(loss='sparse_categorical_crossentropy',
                   optimizer='adam',
                   metrics=['accuracy'])

    modelI.load_weights('model_saved.h5')

    sess = keras.backend.get_session()
    # image = request.args.get('image', default = 1, type = str)
    print("------------------")
    print(image)
    print("------------------")
    img = tensorflow.compat.v1.read_file(image)
    img = tensorflow.compat.v1.image.decode_jpeg(img, channels=3)
    img.set_shape([None, None, 3])
    img = tensorflow.compat.v1.image.resize_images(img, (350, 350))
    img = img.eval(session=sess)  # convert to numpy array
    img = np.expand_dims(img, 0)  # make 'batch' of 1

    pred = modelI.predict(img)
    # pred = labels["label_names"][np.argmax(pred)]
    print(pred)
    # y = ["Empty sheet", "Not empty sheet"]
    y = ["Real", "Fake"]
    print(np.argmax(pred))
    print(y[np.argmax(pred)])
    return y[np.argmax(pred)]


getImageClass("WIN_20210811_18_11_32_Pro 20.jpg")
