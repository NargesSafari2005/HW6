class DAS:
    def __init__(self):
        self.Patients = {}
        self.Schedule = {}
    def executeCommand(self, command):
        tokens = command.split()
        if len(tokens) == 0:
            print("invalid command")
            return
        if tokens[0] == "add" and tokens[1] == "patient":
            self.addPatient(tokens[2:])
        elif tokens[0] == "display" and tokens[1] == "patient":
            self.displayPatient(tokens[2:])
        elif tokens[0] == "add" and tokens[1] == "visit":
            self.addVisit(tokens[2:])
        elif tokens[0] == "delete" and tokens[1] == "patient":
            self.deletePatient(tokens[2:])
        elif tokens[0] == "display" and tokens[1] == "visit" and tokens[2] == "list":
            self.displayVisitList()
        elif tokens[0] == "exit":
            exit()
        else:
            print("invalid command")

    def addPatient(self, args):
        patientID, name, familyName, age, height, weight = map(str, args)
        if int(patientID) in self.Patients:
            print("error: this ID already exists")
        elif int(age) < 0:
            print("error: invalid age")
        elif int(height) < 0:
            print("error: invalid height")
        elif int(weight) < 0:
            print("error: invalid weight")
        else:
            self.Patients[int(patientID)] = {
                "Name": name,
                "FamilyName": familyName,
                "Age": age,
                "Height": height,
                "Weight": weight
            }
            print("patient added successfully")

    def displayPatient(self, args):
        patientID = int(args[0])
        if patientID not in self.Patients:
            print("error: invalid ID")
        else:
            patientInfo = self.Patients[patientID]
            print(f"patient name: {patientInfo['Name']}")
            print(f"patient family name: {patientInfo['FamilyName']}")
            print(f"patient age: {patientInfo['Age']}")
            print(f"patient height: {patientInfo['Height']}")
            print(f"patient weight: {patientInfo['Weight']}")

    def deletePatient(self, args):
        patientID = int(args[0])
        if patientID not in self.Patients:
            print("error: invalid id")
        else:
            deletedPatientInfo = self.Patients.pop(patientID)
            for time, visitInfo in list(self.Schedule.items()):
                if visitInfo.startswith(f"({deletedPatientInfo['Name']}) ({deletedPatientInfo['FamilyName']})"):
                    del self.Schedule[time]
            print("patient deleted successfully!")

    def addVisit(self, args):
        patientID, visitTime = map(int, args)
        if patientID not in self.Patients:
            print("error: invalid id")
        elif visitTime < 9 or visitTime > 18:
            print("error: invalid time")
        elif visitTime in self.Schedule:
            print("error: busy time")
        else:
            self.Schedule[visitTime] = f"({self.Patients[patientID]['Name']}) ({self.Patients[patientID]['FamilyName']})"
            print("visit added successfully!")

    def displayVisitList(self):
        print("SCHEDULE:")
        for time, visitInfo in self.Schedule.items():
            visitInfo = visitInfo.replace('(', '').replace(')', '')
            print(f"{time}:00 {visitInfo}")


if __name__ == "__main__":
    scheduler = DAS()
    while True:
        try:
            command = input()
            scheduler.executeCommand(command)
        except EOFError:
            break