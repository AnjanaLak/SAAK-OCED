import speech_recognition as sr
import time
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import audio_feature_extraction as get_features
import neural_network

def get_numpy_array(features_df):
    X = np.array(features_df.feature.tolist())
    y = np.array(features_df.class_label.tolist())
    # encode classification labels
    le = LabelEncoder()
    # one hot encoded labels
    yy = to_categorical(le.fit_transform(y))
    return X, yy, le


def get_train_test(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# capture starting time
start = time.time()

# audio file
file_path = "sample.wav"


# function of the audio chunk and speech recognize
def text_conversation_using_chunks(file_path):

    # open the audio file
    sound = AudioSegment.from_wav(file_path)
    print(sound)

    print("Processing chunks...")

    # split audio
    # min_silence_len - minimum silent length (0.5 seconds or 500 ms)
    # silence_thresh - silent quieter than 14 dBFS
    # keep_silence - amount of silence to leave at the beginning and end of the each chunk
    chunks = split_on_silence(sound, min_silence_len=50, silence_thresh=sound.dBFS - 16, keep_silence=150)

    chunk_folder_name = "Audio_chunks"

    # create folder to store chunks
    if not os.path.isdir(chunk_folder_name):
        os.mkdir(chunk_folder_name)

    # text_folder = "text_folder"
    # if not os.path.isdir(text_folder):
    # os.mkdir(text_folder)
    full_text_nn = ""

    for i, audio_chunk in enumerate(chunks, start=1):

        # export audio chunks to Audio_chunks folder
        chunk_file = os.path.join(chunk_folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_file, format="wav", bitrate='192k')

        # recognize the chunk
        with sr.AudioFile(chunk_file) as source:

            try:
                print("Extracting features..")
                features_df = get_features.extract_features()

                # convert into numpy array
                X, y, le = get_numpy_array(features_df)
                word_nn = neural_network.predict(chunk_file, le, "trained_cnn.h5")

            # catch errors
            except sr.UnknownValueError as e:
                print("Error: ", str(e))
            else:
                full_text_nn += word_nn
                full_text_nn += " "

    # return text of all chunks
    print("\nConverted text (Neural Networl): ", full_text_nn)
    return full_text_nn


text_conversation_using_chunks(file_path)


# identify response time
# current time - start time
print("response time in seconds")
print(time.time() - start)
