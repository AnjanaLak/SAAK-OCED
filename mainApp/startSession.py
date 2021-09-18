import os

import directoryManager


def create_session(candidateID, candidateName, candidateEmail, examID, examDate, duration, uniID, img):
    # to create directories
    directoryManager.createDirectories(candidateID, examID)
    # to save the user image to the directory and return directory path
    image_stored_dir = storeProfilePic(candidateID, img)
    print(image_stored_dir)
    # need to insert user image path to the session and candidate table records
    # need to insert records into session table
    # need to insert records into User table
    # need to insert records into Exam table
    # print(os.getcwd())
    cwd = os.getcwd()


def storeProfilePic(cid, cimg):
    cd = os.getcwd()
    os.chdir(cd + '/ProfilePhoto')

    cimg.save(f'{cid}.png')
    storedDir = str(os.getcwd() + f'\{cid}.png')
    print(storedDir)
    os.chdir(cd)
    print(os.getcwd())
    return storedDir
