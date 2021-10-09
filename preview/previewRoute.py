############ Routes #################################################################

from flask import jsonify
from frameCaptureService import app2
from sessions import audioMain
from flask import Flask, request
from faceRecognition import test2


@app2.route('/startPreview', methods=['POST'])
def start_Preview():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    # need to call frame divider ?????
    x = test2.start_user_recognition(candidateID, examinationID)
    # Need to call face_recognition, rough paper detection, area allocation
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})

