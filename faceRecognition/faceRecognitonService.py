import os
import cv2
import time
from faceRecognition import CompareFaces
from mainApp import db
from mainApp.models import Face_Recog_Record
from datetime import datetime

prof_photo_dir = '../ProfilePhoto/'
frames_dir = '../Frames/'


def start_user_recognition(candidateID, examID):
    i = 0
    candidate_id_photo = prof_photo_dir + candidateID + ".png"
    print("the current working directory is =>" + os.getcwd())
    os.chdir(os.getcwd() + '/faceRecognition/')
    while True:
        i += 1
        start_time = time.time()
        try:
            fileName = frames_dir + candidateID + "/" + examID + "/" + "device_mounted_camera_frames/" + \
                       str(i) + ".png"
            checkFalse = CompareFaces.compareFaces(candidate_id_photo, fileName, 0.5)
            if checkFalse == 'False':
                # need to create a record if violation occurred
                framesDir = os.getcwd() + fileName
                record = Face_Recog_Record(candidateID, examID, framesDir, datetime.now())  # creating an article object
                db.session.add(record)  # adding the record to the object
                try:
                    db.session.commit()
                    print("Violation record added")
                except Exception as e:
                    print(e)

        except:
            print("The directory is empty or Process completed successfully")
            break
        time.sleep(0.1)  # sleep time in seconds
        #         # print("--- %s seconds ---" % (time.time() - start_time))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    os.chdir('../')
