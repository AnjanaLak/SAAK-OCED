import os
from mainApp import models

print(os.getcwd())
frames_dir = '../Reports/'


def text_file_generator(candidateID, examinationID):
    print("the current working directory is =>" + os.getcwd())
    os.chdir(os.getcwd() + '/reportGenerator/')
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    print(fileDir + " = The fileDir")
    location = frames_dir + candidateID + "/" + examinationID + "/" + "report" + ".txt"
    filename = os.path.join(fileDir, location)
    filename = os.path.abspath(os.path.realpath(filename))
    print(filename + " = The filename")
    f = open(filename, "w")
    f.write("###################################### Violation Report ###################################### \n")
    f.write("\n")
    f.write("##Student ID =>" + candidateID + "\n")
    f.write("##Exam ID =>" + examinationID + "\n")
    f.write("\n")
    f.write("######### Records #############################################################################\n")
    f.write("\n")
    f.write("\n")
    ### Print Audio Violations
    f.write("1) Audio Violation Records, \n")
    f.write("Data record order => Chunk Directory|| Processed Time || {Keywords}")
    f.write("\n")
    f.write("\n")
    # x = models.Audio_Record.query.all()
    audio_results = models.Audio_Record.query.filter_by(candidateID=candidateID, examID=examinationID).all()
    for rec in audio_results:
        row = rec.chunkDirectory + ", " + str(rec.processed_time) + ", " + "{" + rec.keywords + "}"
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")
    ### Print Face Recognition Violations
    f.write("2) Face Recognition Violations, \n")
    f.write("Data record order => Frame Directory|| Processed Time")
    f.write("\n")
    f.write("\n")
    face_rec_results = models.Face_Recog_Record.query.filter_by(candidateID=candidateID, examID=examinationID).all()
    for face_rec_rec in face_rec_results:
        row = face_rec_rec.frameDirectory + ", " + str(face_rec_rec.processed_time)
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")
    ### Print Spoofed Face Violations
    f.write("3) Spoofed Face Violations, \n")
    f.write("Data record order => Frame Directory|| Processed Time")
    f.write("\n")
    f.write("\n")
    face_spoofed_results = models.Face_Spoofed_Record.query.filter_by(candidateID=candidateID,
                                                                      examID=examinationID).all()
    for face_sp_rec in face_spoofed_results:
        row = face_sp_rec.frameDirectory + ", " + str(face_sp_rec.processed_time)
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")
    ### Print Rough Paper Violations
    f.write("4) Rough Paper Violations, \n")
    f.write("Data record order => Frame Directory|| Processed Time")
    f.write("\n")
    f.write("\n")
    rough_ppr_results = models.Rough_Ppr_Record.query.filter_by(candidateID=candidateID,
                                                                examID=examinationID).all()
    for ru_ppr_rec in rough_ppr_results:
        row = ru_ppr_rec.frameDirectory + ", " + str(ru_ppr_rec.processed_time)
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")
    ### Human Movements Violations
    f.write("5) Human Movements Violations, \n")
    f.write("Data record order => Frame Directory|| Processed Time")
    f.write("\n")
    f.write("\n")
    hm_results = models.Human_Movement_Record.query.filter_by(candidateID=candidateID,
                                                              examID=examinationID).all()
    for hm_rec in hm_results:
        row = hm_rec.frameDirectory + ", " + str(hm_rec.processed_time)
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")
    ### Allocated Area Violations
    f.write("6) Allocated Area Violations, \n")
    f.write("Data record order => Frame Directory|| Processed Time")
    f.write("\n")
    f.write("\n")
    aa_results = models.Allocated_Area_Record.query.filter_by(candidateID=candidateID,
                                                              examID=examinationID).all()
    for aa_rec in aa_results:
        row = aa_rec.frameDirectory + ", " + str(aa_rec.processed_time)
        f.write(row + "\n")
    f.write("\n")
    f.write("\n")

    ########################## closing the file ###############
    f.close()
    os.chdir('../')

# text_file_generator("IT17019750", "IT4000")
# fileDir = os.path.dirname(os.path.realpath('__file__'))
# print(fileDir)
#
# filename = os.path.join(fileDir, '../Folder2/same.txt')
# filename = os.path.abspath(os.path.realpath(filename))
# print(filename)
