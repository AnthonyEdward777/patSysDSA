class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.contactEmail = ""
        self.medicalHistory = ""
        self.severity_score = 0
        self.room_number = 0

    def setContact(self, contact):
        self.contactEmail = contact

    def setHistory(self, history):
        self.medicalHistory = history

    def setSeverity(self, severity):
        self.severity_score = severity

    def setRoom(self, room):
        self.room_number = room

    def getContact(self):
        return self.contactEmail

    def getHistory(self):
        return self.medicalHistory

    def getSeverity(self):
        return self.severity_score

    def getRoom(self):
        return self.room_number
