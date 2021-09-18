import os


def createDirectories(candidateID, examID):
    candidateID = candidateID
    examID = examID
    cwd = os.getcwd()
    # os.chdir(cwd + '/../')
    cd = os.getcwd()
    print(cd)

    # calling function to create AudioChunks Directory
    createAudioChunksDirectory(candidateID, examID, cd)
    # calling function to create AudioRecords Directory
    createAudioRecordsDirectory(candidateID, examID, cd)
    # calling function to create Frames Directory
    createFramesDirectory(candidateID, examID, cd)
    # calling function to create Reports Directory
    createReportsDirectory(candidateID, examID, cd)
    # calling function to ViolationProofs Directory
    ViolationProofsDirectory(candidateID, examID, cd)

    os.chdir(cd)

def createAudioChunksDirectory(candidateID, examID, cd):
    try:
        os.chdir(cd + '/AudioChunks/')
        os.mkdir(candidateID)
    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/AudioChunks/' + candidateID + '/')
        os.mkdir(examID)

    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/AudioChunks/' + candidateID + '/' + examID + '/')
        os.mkdir('audio_chunks')

    except(FileExistsError):
        os.chdir(cd)
        pass

    os.chdir(cd)

def createAudioRecordsDirectory(candidateID, examID, cd):
    try:
        os.chdir(cd + '/AudioRecords/')
        os.mkdir(candidateID)
    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/AudioRecords/' + candidateID + '/')
        os.mkdir(examID)

    except(FileExistsError):
        os.chdir(cd)
        pass

    os.chdir(cd)

def createFramesDirectory(candidateID, examID, cd):
    try:
        os.chdir(cd + '/Frames/')
        os.mkdir(candidateID)
    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/Frames/' + candidateID + '/')
        os.mkdir(examID)

    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/Frames/' + candidateID + '/' + examID + '/')
        os.mkdir('face_camera_frames')

    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/Frames/' + candidateID + '/' + examID + '/')
        os.mkdir('device_mounted_camera_frames')

    except(FileExistsError):
        os.chdir(cd)
        pass

    os.chdir(cd)

def createReportsDirectory(candidateID, examID, cd):
    try:
        os.chdir(cd + '/Reports/')
        os.mkdir(candidateID)
    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/Reports/' + candidateID + '/')
        os.mkdir(examID)

    except(FileExistsError):
        os.chdir(cd)
        pass
    os.chdir(cd)

def ViolationProofsDirectory(candidateID, examID, cd):
    try:
        os.chdir(cd + '/ViolationProofs/')
        os.mkdir(candidateID)
    except(FileExistsError):
        os.chdir(cd)
        pass

    try:
        os.chdir(cd + '/ViolationProofs/' + candidateID + '/')
        os.mkdir(examID)

    except(FileExistsError):
        os.chdir(cd)
        pass
    os.chdir(cd)
