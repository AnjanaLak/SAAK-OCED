from datetime import datetime
from mainApp import db
from mainApp import ma


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
    duration = db.Column(db.String(20))
    status = db.Column(db.Integer, default=0)

    def __init__(self, candidateID, examID, examDate, duration, status):
        self.candidateID = candidateID
        self.examID = examID
        self.examDate = examDate
        self.duration = duration
        self.status = status


### Class Report ###############################################################################################


############################################### Records ########################################################

### Audio Record

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


### face recognition record

class Face_Recog_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    frameDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, frameDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.frameDirectory = frameDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.frameDirectory}',  '{self.processed_time}')"


### spoofed face record

class Face_Spoofed_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    frameDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, frameDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.frameDirectory = frameDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Face_Spoofed_Record('{self.candidateID}', '{self.examID}', '{self.frameDirectory}', " \
               f" '{self.processed_time}')"


### Rough paper record

class Rough_Ppr_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    frameDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, frameDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.frameDirectory = frameDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.frameDirectory}',  '{self.processed_time}')"


###  Human movements record

class Human_Movement_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    frameDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, frameDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.frameDirectory = frameDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.frameDirectory}',  '{self.processed_time}')"


###  Allocation area violation record

class Allocated_Area_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    frameDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, frameDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.frameDirectory = frameDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.frameDirectory}',  '{self.processed_time}')"


### Extension connectivity violation record

class Extension_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    violationType = db.Column(db.String(20))
    screenshotDirectory = db.Column(db.String(500))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, violationType, screenshotDirectory, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.violationType = violationType
        self.screenshotDirectory = screenshotDirectory
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.violationType}'," \
               f" '{self.screenshotDirectory}',  '{self.processed_time}') "


### Microphone disable record

class Microphone_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}',  '{self.processed_time}')"


### Camera disable record
class Camera_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateID = db.Column(db.String(20))
    examID = db.Column(db.String(20))
    camType = db.Column(db.String(1))  # 'f' || 'd'
    processed_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, candidateID, examID, camType, processed_time):
        self.candidateID = candidateID
        self.examID = examID
        self.camType = camType
        self.processed_time = processed_time

    def __repr__(self):
        return f"Audio_Record('{self.candidateID}', '{self.examID}', '{self.camType}', '{self.processed_time}')"


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
        fields = ('candidateID', 'examID', 'examDate', 'duration', 'status')


exam_Schema = Exam_Schema()
exam_Schema = Exam_Schema(many=True)
