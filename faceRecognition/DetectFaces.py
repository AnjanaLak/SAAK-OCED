import face_recognition
import time
from PIL import Image

# Note => If face_recognition failed to install use => pip3 install face_recognition

def getFacesLocations(imagePath):
    start_time = time.time()
    image = face_recognition.load_image_file(imagePath)
    face_locations = face_recognition.face_locations(image)
    print("--- %s seconds ---" % (time.time() - start_time))
    # top, right, bottom, left = face_locations[0]
    # face_image1 = image[top:bottom, left:right]
    # image_save = Image.fromarray(face_image1)
    # image_save.save("image_1.jpg")
    return face_locations
