import face_recognition
import time


def compareFaces(faceImagePath1, faceImagePath2, tolerance):
    start_time = time.time()
    image1 = face_recognition.load_image_file(faceImagePath1)
    image2 = face_recognition.load_image_file(faceImagePath2)

    encoding_1 = face_recognition.face_encodings(image1)[0]

    try:
        encoding_2 = face_recognition.face_encodings(image2)[0]
        results = face_recognition.compare_faces([encoding_1], encoding_2, tolerance=tolerance)
        # if 'False' in r:
        #     results = 'False'
    except:
        print()
        results = "Face is not exposed to the camera properly"

    print(results)
    print(type(results))
    print("--- %s seconds ---" % (time.time() - start_time))
    return results
