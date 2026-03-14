from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_registered = datetime.now()

    def display(self):
        return f"{self.name} registered at {self.time_registered}"