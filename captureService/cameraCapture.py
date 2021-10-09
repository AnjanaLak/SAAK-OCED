import os
import time
import cv2
import threading


class camThread(threading.Thread):
    def __init__(self, previewName, camID, candidateID, examinationID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.candidateID = candidateID
        self.examinationID = examinationID

    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID, self.candidateID, self.examinationID)


def camPreview(previewName, camID, candidateID, examinationID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False

    i = 0
    os.chdir(os.getcwd() + '/captureService/')
    frames_dir = '../Frames/'
    while rval:
        i += 1
        # cv2.imshow(previewName, frame)
        rval, frame = cam.read()

        if camID == 0:
            print(os.getcwd() + "is the face cam frame saving directory" + " with i value : " + str(i))
            file_name = frames_dir + candidateID + "/" + examinationID + "/" + "face_camera_frames/" + \
                        str(i) + ".png"
            cv2.imwrite(file_name, frame)
        if camID == 1:
            print(os.getcwd() + "is the  device cam frame saving directory" + " with i value : " + str(i))
            file_name = frames_dir + candidateID + "/" + examinationID + "/" + "device_mounted_camera_frames/" + \
                        str(i) + ".png"
            cv2.imwrite(file_name, frame)

        time.sleep(4)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    os.chdir('../')
    cv2.destroyWindow(previewName)


def camerasCaptureStart(candidateID, examinationID):
    print("the current working directory is =>" + os.getcwd())
    # Creating threads to each face camera and device mounted camera
    thread1 = camThread("Face Mounted Camera", 0, candidateID, examinationID)
    #thread2 = camThread("Device Mounted Camera", 1, candidateID, examinationID)

    thread1.start()
    #thread2.start()
    print()
    print("Active threads", threading.activeCount())
