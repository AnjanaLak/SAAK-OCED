############ Routes #################################################################
from time import sleep

from flask import jsonify

from MultiUserDetection.StaticDynamicDetectionService import predict_human_movements
from RoughPaper.predict_image_class import predict_rough_papers
from areaAllocation.headAngleEstimation import predictAngleEstimations
from mainApp import app, db
from mainApp.models import Session
from reportGenerator.textFileGenerator import text_file_generator
from sessions import audioMain
from flask import Flask, request
from PIL import Image
from mainApp import startSession
from captureService import cameraCapture
from faceRecognition import faceRecognitonService
import requests
from faceSpoofing import predict_image_class

global x


@app.route('/examSession', methods=['POST'])
def start_session():
    cid = request.form['candidateID']
    cname = request.form['candidateName']
    cemail = request.form['candidateEmail']
    eid = request.form['ExamID']
    edate = request.form['examDate']
    uid = request.form['uniID']
    dur = request.form['duration']
    cimg = request.files['image']
    startSession.create_session(cid, cname, cemail, eid, edate, dur, uid, cimg)
    session_info = session_info_to_frontend(cid, cname, cemail, eid, edate, dur, uid)
    return jsonify(session_info)
    # image = Image.open(cimg.stream)
    # Calling create_session function from startSession.py


@app.route('/processExam', methods=['POST'])
def process_exam():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    # Need to call audio_classification,face_recognition, rough paper detection, area allocation
    audioMain.start(candidateID, examinationID)
    predictAngleEstimations(candidateID, examinationID)
    sleep(1)
    predict_human_movements(candidateID, examinationID)
    faceRecognitonService.start_user_recognition(candidateID, examinationID)
    predict_image_class.predict_spoofed_frames(candidateID, examinationID)
    predict_rough_papers(candidateID, examinationID)
    # need to retrieve data from db and generate a text file
    x = text_file_generator(candidateID, examinationID)
    if x:
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})


@app.route('/uploadRoughPaper', methods=['POST'])
def upload_rough_paper():
    cimg = request.files['file']
    image = Image.open(cimg.stream)
    # Calling save rough paper function
    print(image)

    return jsonify({"Status": "Completed"})


### post request to send session info to the front end
def session_info_to_frontend(cid, cname, cemail, eid, edate, dur, uid):
    # frontend_session_url = ''
    session_info = {'candidateID': cid, 'candidateName': cname, 'candidateEmail': cemail, 'ExamID': eid,
                    'examDate': edate, 'duration': dur, 'uniID': uid}
    return session_info
    # result = requests.post(url=frontend_session_url, data=session_info)
    # r = result.text
    # print(r)

################## under testing #########################################################################


# @app.route('/get/<id>/', methods=['GET'])
# def get_session_info_to_frontend(id):
#     # spllit the candidate_id, uni_id and the secret key
#     print(type(id))
#     # define another get method
#     # session_info = Session.query.get(id)
#     # return session_info
