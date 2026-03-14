from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_registered = datetime.now()

    def get_time(self):
        return self.time_registered.strftime("%I:%M %p")