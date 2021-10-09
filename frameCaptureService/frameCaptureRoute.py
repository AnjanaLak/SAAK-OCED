############ Route to start frame capture #################################################################

from flask import jsonify

from captureService import cameraCapture
from frameCaptureService import app2
from flask import request


@app2.route('/captureCam', methods=['POST'])
def capture_cam():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    x = cameraCapture.camerasCaptureStart(candidateID, examinationID)
    if x == "Completed":
        return jsonify({"Status": "Completed"})
    else:
        return jsonify({"Status": "Not Completed"})


