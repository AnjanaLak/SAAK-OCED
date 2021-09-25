############ Routes #################################################################

from flask import jsonify
from mainApp2 import app2, db
from sessions import audioMain
from flask import Flask, request
from faceRecognition import test2


@app2.route('/startAudioProcess', methods=['POST'])
def process_audio():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    x = audioMain.start(candidateID, examinationID)
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})


@app2.route('/captureAudio', methods=['POST'])
def capture_audio():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    # x = audioMain.start(candidateID, examinationID)
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})


@app2.route('/processExam', methods=['POST'])
def process_exam():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    # need to call frame divider ?????
    # x = audioMain.start(candidateID, examinationID)
    # Need to call face_recognition, rough paper detection, area allocation
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})


@app2.route('/processFaceRecognition', methods=['POST'])
def process_face_recognition():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    # need to call frame divider ?????
    x = test2.start_user_recognition(candidateID, examinationID)
    # Need to call face_recognition, rough paper detection, area allocation
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})

