from Patient import Patient
from Node import Node

class PatientLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def admitPatient(self, name, age, contact, history, severity, room):
        newNode = Node(name, age)

        newNode.data.setContact(contact)
        newNode.data.setHistory(history)
        newNode.data.setSeverity(severity)
        newNode.data.setRoom(room)

        newNode.next = self.head
        self.head = newNode
        self.length += 1

        return newNode

    def dischargePatient(self):
        if self.head is None:
            return None

        discharged_node = self.head
        self.head = self.head.next
        discharged_node.next = None
        self.length -= 1

        return discharged_node

    def changeSeverity(self, name, newSeverity):
        current = self.head

        while current is not None:
            if current.data.name == name:
                current.data.setSeverity(newSeverity)
                return current
            current = current.next

        return None

    def changeRoom(self, name, newRoom):
        current = self.head
        while current is not None:
            if current.data.name == name:
                current.data.setRoom(newRoom)
                return current
            current = current.next

    def displayRecords(self):
        """Betrag3 Python list"""
        current = self.head
        records = []

        while current is not None:
            patient_info = {
                "Name": current.data.name,
                "Age": current.data.age,
                "Contact": current.data.getContact(),
                "Medical History": current.data.getHistory(),
                "Severity Score": current.data.getSeverity(),
                "Room Number": current.data.getRoom()
            }
            records.append(patient_info)
            current = current.next

        return records

    def searchPatient(self, name):
        current = self.head

        while current is not None:
            if current.data.name == name:
                return current
            current = current.next

        return None
    
    def sort_by_severity(self):
        if self.head is None or self.head.next is None:
            return
        
        swapped = True

        while swapped:
            swapped = False
            current = self.head


            while current.next is not None:
                if current.data.getSeverity() > current.next.data.getSeverity():

                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
            
                current = current.next

    def sort_by_severity_desc(self):
        if self.head is None or self.head.next is None:
            return
        
        
        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next is not None:

                if current.data.getSeverity() < current.next.data.getSeverity():
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
            
                current = current.next