import cv2
import time
import DetectFaces
import CompareFaces

vid = cv2.VideoCapture(0)

while (True):
    start_time = time.time()

    ret, frame = vid.read()

    # cv2.imshow('frame', frame)
    cv2.imwrite("frame.png", frame)
    time.sleep(1)
    print("--- %s seconds ---" % (time.time() - start_time))
    faceLocations = DetectFaces.getFacesLocations(str("frame.png"))
    # print(faceLocations)

    i = 0
    filenames = []
    for faceLocation in faceLocations:
        i += 1
        print(faceLocation)
        x = faceLocation[3]
        y = faceLocation[0]
        h = faceLocation[1] - x
        w = faceLocation[2] - y
        img = cv2.imread("frame.png")  # photo of real user
        crop_img = img[y:y + h, x:x + w]
        ts = time.time()
        faceFileName = "face_" + str(ts) + "_" + str(i) + ".png"
        filenames.append(faceFileName)
        cv2.imwrite("faces_detected/" + faceFileName, crop_img)
        print(CompareFaces.compareFaces("registered_user_faces/image.png", "faces_detected/" + faceFileName, 0.5))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
