from collections import deque
from models import Patient

class QueueManager:
    def __init__(self):
        self.queue = deque()
        self.patients_seen = 0
        self.last_called = None 
        self.history = []

    def add_patient(self, name):
        patient = Patient(name)
        self.queue.append(patient)

    def next_patient(self):
        if self.queue:
            patient = self.queue.popleft()
            self.patients_seen += 1
            self.last_called = patient.name
            self.history.append(patient.name)
            return patient

    def get_queue(self):
        return list(self.queue)
    
    def clear_queue(self):
        self.queue.clear()