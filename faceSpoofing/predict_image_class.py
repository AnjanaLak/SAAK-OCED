import os
import time

from keras.layers import Activation
import keras
import numpy as np
import tensorflow
from keras import backend as K
from keras.layers import Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential
from datetime import datetime

from mainApp import db
from mainApp.models import Face_Spoofed_Record

frames_dir = '../Frames/'


def getImageClass():
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

    # modelI.load_weights('model_saved.h5')
    modelI.load_weights('model_saved.h5')
    return modelI


def predict_spoofed_frames(candidateID, examinationID):
    print("the current working directory is =>" + os.getcwd())
    os.chdir(os.getcwd() + '/faceSpoofing/')
    modelI = getImageClass()
    i = 0
    while True:
        i += 1
        start_time = time.time()
        try:
            frame = frames_dir + candidateID + "/" + examinationID + "/" + "device_mounted_camera_frames/" + \
                    str(i) + ".png"
            # print(CompareFaces.compareFaces(candidate_id_photo, fileName, 0.5))
            sess = keras.backend.get_session()
            # image = request.args.get('image', default = 1, type = str)
            print("------------------")
            print(frame)
            print("------------------")
            img = tensorflow.compat.v1.read_file(frame)
            img = tensorflow.compat.v1.image.decode_jpeg(img, channels=3)
            img.set_shape([None, None, 3])
            img = tensorflow.compat.v1.image.resize_images(img, (350, 350))
            img = img.eval(session=sess)
            img = np.expand_dims(img, 0)

            pred = modelI.predict(img)
            print(pred)
            y = ["Real", "Fake"]
            print(np.argmax(pred))
            print(y[np.argmax(pred)])
            print(type(y[np.argmax(pred)]))
            # return y[np.argmax(pred)]
            # need to create a record if violation occurred
            if y[np.argmax(pred)] == "Real":
                print("This is fake")
                print(candidateID)
                # print(type(candidateID) + "is the type of candidate ID")
                print(examinationID)
                framesDir = os.getcwd() + frames_dir + candidateID + "/" + examinationID + "/" + \
                            "device_mounted_camera_frames/" + \
                            str(i) + ".png"
                print(framesDir)
                record = Face_Spoofed_Record(candidateID, examinationID, framesDir, datetime.now())  # creating an article object
                db.session.add(record)  # adding the record to the object
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    pass


        except:
            print("The directory is empty")
            break
        time.sleep(0.3)  # sleep time in seconds
        #         # print("--- %s seconds ---" % (time.time() - start_time))
    os.chdir('../')