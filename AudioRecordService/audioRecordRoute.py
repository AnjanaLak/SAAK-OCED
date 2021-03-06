############ Route to start record audio #################################################################

from flask import jsonify
from AudioRecordService import app1
from flask import request
from AudioRecorder.record import RecordAudio


@app1.route('/captureAudio', methods=['POST'])
def capture_audio():
    candidateID = request.json['studentID']
    examinationID = request.json['examID']
    RecordAudio(candidateID, examinationID)
    return jsonify({"Status": "Record Completed"})


