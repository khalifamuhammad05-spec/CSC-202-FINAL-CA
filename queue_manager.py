from collections import deque
from models import Patient

class QueueManager:
    def __init__(self):
        self.queue = deque()
        self.patients_seen = 0

    def add_patient(self, name):
        patient = Patient(name)
        self.queue.append(patient)

    def next_patient(self):
        if self.queue:
            self.patients_seen += 1
            return self.queue.popleft()

    def get_queue(self):
        return list(self.queue)