from Patient import Patient
class Node:
    def __init__(self, name, age):
        self.data = Patient(name, age)
        self.next = None
    