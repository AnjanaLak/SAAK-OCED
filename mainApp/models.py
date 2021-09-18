from datetime import datetime
from audioClassification import db
from audioClassification import ma


#################### DB models ######################################################################
#####################################################################################################

### Class Session ###################################################################################

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20), unique=True)
    candidateName = db.Column(db.String(50))
    candidateEmail = db.Column(db.String(50))
    examID = db.Column(db.String(20))
    examDate = db.Column(db.String(20))
    duration = db.Column(db.String(20))
    uniID = db.Column(db.String(20))
    imagePath = db.Column(db.String(100))

    def __init__(self, candidateID, candidateName, candidateEmail, examID, examDate, duration, uniID, imagePath):
        self.candidateID = candidateID
        self.candidateName = candidateName
        self.candidateEmail = candidateEmail
        self.examID = examID
        self.examDate = examDate
        self.duration = duration
        self.uniID = uniID
        self.imagePath = imagePath


### Class Candidate ###############################################################################################

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20), unique=True)
    candidateName = db.Column(db.String(50))
    candidateEmail = db.Column(db.String(50))
    imagePath = db.Column(db.String(100))

    def __init__(self, candidateID, candidateName, candidateEmail, imagePath):
        self.candidateID = candidateID
        self.candidateName = candidateName
        self.candidateEmail = candidateEmail
        self.imagePath = imagePath


### Class Exam ###############################################################################################

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    examDate = db.Column(db.String(20))
    dateAttempted = db.Column(db.String(20))
    duration = db.Column(db.String(20))
    status = db.Column(db.Integer)

    def __init__(self, candidateID, examID, examDate, dateAttempted, duration, status):
        self.candidateID = candidateID
        self.examID = examID
        self.examDate = examDate
        self.dateAttempted = dateAttempted
        self.duration = duration
        self.status = status


### Class Report ###############################################################################################


############################################### Records ########################################################

class Audio_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    chunkDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)
    keywords = db.Column(db.String(500))

    def __init__(self, candidateID, examID, chunkDirectory, processed_time, keywords):
        self.candidateID = candidateID
        self.examID = examID
        self.chunkDirectory = chunkDirectory
        self.processed_time = processed_time
        self.keywords = keywords

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.chunkDirectory}',  '{self.processed_time}', " \
               f"'{self.keywords}')"


################################################ SCHEMAS ############################################################
#####################################################################################################################

class Audio_Record_Schema(ma.Schema):
    class Meta:
        fields = ('candidateID', 'examID', 'chunkDirectory', 'processed_time', 'keywords')


audio_Record_Schema = Audio_Record_Schema()
audio_Record_Schemas = Audio_Record_Schema(many=True)


class Session_Schema(ma.Schema):
    class Meta:
        fields = ('candidateID', 'candidateName', 'candidateEmail', 'examID', 'examDate', 'duration',
                  'uniID', 'imagePath')


session_Schema = Session_Schema()
session_Schemas = Session_Schema(many=True)


class Candidate_Schema(ma.Schema):
    class Meta:
        fields = ('candidateID', 'candidateName', 'candidateEmail', 'imagePath')


candidate_Schema = Candidate_Schema()
candidate_Schema = Candidate_Schema(many=True)



class Exam_Schema(ma.Schema):
    class Meta:
        fields = ('candidateID', 'examID', 'examDate', 'dateAttempted', 'duration', 'status')


Exam_Schema = Exam_Schema()
Exam_Schema = Exam_Schema(many=True)

