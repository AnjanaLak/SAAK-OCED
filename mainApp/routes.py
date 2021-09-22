############ Routes #################################################################

from flask import jsonify
from mainApp import app, db
from mainApp.models import Session
from flask import Flask, request
from PIL import Image
from mainApp import startSession
import requests


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
    # image = Image.open(cimg.stream)
    # Calling create_session function from startSession.py
    startSession.create_session(cid, cname, cemail, eid, edate, dur, uid, cimg)
    # session_info_to_frontend(cid, cname, cemail, eid, edate, dur, uid, cimg)
    return jsonify({"Status": "Session Registration Completed"})


@app.route('/get/<id>/', methods=['GET'])
def get_session_info_to_frontend(id):
    # spllit the candidate_id, uni_id and the secret key
    print(type(id))
    # define another get method
    # session_info = Session.query.get(id)
    # return session_info


### post request to send session info to the front end
def session_info_to_frontend(cid, cname, cemail, eid, edate, dur, uid, cimg):
    frontend_session_url = ''
    session_info = {'candidateID': cid, 'candidateName': cname, 'candidateEmail': cemail, 'ExamID': eid,
                    'examDate': edate, 'duration': dur, 'uniID': uid, 'image': cimg}
    result = requests.post(url=frontend_session_url, data=session_info)
    r = result.text
    print(r)

# @app.route('/startAudioProcess', methods=['POST'])
# def process_audio():
#     audio_path = request.json['path']
#     candidateID = request.json['studentID']
#     examinationID = request.json['examID']
#     x = main.start(audio_path, candidateID, examinationID)
#     if x == "Completed":
#         return jsonify({"Status": "Completed"})
#     else:
#         return jsonify({"Status": "Not Completed"})
