import os

import cv2
import time
import CompareFaces

vid = cv2.VideoCapture(0)

prof_photo_dir = '../ProfilePhoto/'
frames_dir = '../Frames/'


def start_user_recognition(vid, candidateID, examID):
    i = 0
    candidate_id_photo = prof_photo_dir + candidateID + ".png"
    while True:
        i += 1
        start_time = time.time()
        ret, frame = vid.read()
        fileName = frames_dir + candidateID + "/" + examID + "/" + "device_mounted_camera_frames/" + \
                   str(i) + ".png"
        print(fileName)
        cv2.imwrite(fileName, frame)
        time.sleep(1)  # sleep time in seconds
#         # print("--- %s seconds ---" % (time.time() - start_time))
        print(CompareFaces.compareFaces(candidate_id_photo, fileName, 0.5))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


vid.release()
cv2.destroyAllWindows()

start_user_recognition(vid, 'IT17019750', 'IT4000')
