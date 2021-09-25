import os
import multiprocessing
import directoryManager
from mainApp.models import Session, Candidate, Exam

from mainApp import db
import captureService


def create_session(candidateID, candidateName, candidateEmail, examID, examDate, duration, uniID, img):
    # to create directories
    directoryManager.createDirectories(candidateID, examID)
    # to save the user image to the directory and return directory path
    image_stored_dir = storeProfilePic(candidateID, img)
    print(image_stored_dir)

    # need to insert user image path to the session and candidate table records
    # need to insert records into session table
    session_record = Session(candidateID, candidateName, candidateEmail, examID,
                             examDate, duration, uniID, image_stored_dir)
    db.session.add(session_record)
    try:
        db.session.commit()
    except Exception as e:
        print(e)

    # need to insert records into Candidate table
    candidate_record = Candidate(candidateID, candidateName, candidateEmail, image_stored_dir)
    db.session.add(candidate_record)
    try:
        db.session.commit()
    except Exception as e:
        print(e)

    # need to insert records into Exam table
    # to retrieve the exam status
    status = setProcessStatus(candidateID, examID)
    exam_record = Exam(candidateID, examID, examDate, duration, status)
    db.session.add(exam_record)
    try:
        db.session.commit()
    except Exception as e:
        print(e)


def storeProfilePic(cid, cimg):
    cd = os.getcwd()
    os.chdir(cd + '/ProfilePhoto')

    cimg.save(f'{cid}.png')
    storedDir = str(os.getcwd() + f'\{cid}.png')
    print(storedDir)
    os.chdir(cd)
    print(os.getcwd())
    return storedDir


def setProcessStatus(candidateID, examID):
    # if processStatus():
    #     status = 1
    # else:
    #     status = 0
    status = 0
    return status


def processStatus(candidateID, examID):
    # need to run this function when processing the relevant examination
    return


def initializeExam(candidateID, examID):
    # need to start video streams, save frames, record audio files, trigger user recognition and
    # area allocation
    ## Threading requires to run each functions parallel
    # startAudioRecording()
    return
