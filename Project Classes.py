from tabulate import tabulate

print("\nWelcome to Alberta Hospital (AH) Management system\n")
patients_list = []
class Facilities:
    def __init__(self,facilities):
        self.facilities = facilities
    
    def get_facilities(self):
        return self.facilities


    def displayFacilities(self):
        file = open("facilities.txt", "r")
        print(file.read(-1))

    def writeListOfFacilitiesToFile(self):
        self.facilities_list = Facilities
        file = open("facilities.txt", 'w')
        for i in range(len(Facilities.facilities_list)):
            file.write(self.facilities_list)

    def addFacility(self):
        file = open("facilities.txt", 'a')
        newfacility = input("Enter the facility name: ")
        file.write(newfacility)
        file.close()


class Patients:

    def __init__(self, pid, name, disease, gender, age):
        self.pid = int(pid)
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = int(age)
    
    @staticmethod
    def readPatientsFile():
        patients = []
        file = open("patients.txt", 'r')
        patientfile = file.readlines()
        for line in patientfile:
            patients.append(line.strip())
        for i in range(len(patients)):
            patients_list.append(patients[i].split("_"))
            return patients_list

    @classmethod
    def displayPatientsInfo(self):
        file1 = open("patients.txt", "r")
        print(file1.read(-1))

    def formatPatientsInfo(self):
        return f"{self.pid}_ {self.name}_{self.disease}_{self.gender}_{self.age}"


   
    def enterPatientInfo(self):
        self.pid = input("Enter Patient ID:")
        self.name = input("Enter Patient name:")
        self.disease = input("Enter Patient disease:")
        self.gender = input("Enter Patient gender: ")
        self.age = (input("Enter Patient age:"))
        patients_list = [self.pid, self.name, self.disease, self.gender, self.age]
        patients_list.insert(1,"_")
        patients_list.insert(3,"_")
        patients_list.insert(5,"_")
        patients_list.insert(7,"_")
        res= ''.join([str(item)for item in patients_list])
        return res
    def addPatientToFile(patients):
        with open("patients.txt",'a') as f:
            f.write(f'{patients}\n')
    
    def searchPatientById(patients_list):
        patient_id = input("Enter the Patient ID: ")
        for i in range(len(patients_list)):
            if patients_list[i][0] == patient_id:
                return patients_list[i]


        
        





class Management:
    selection = int(input("Select from the following options, or select 0 to stop\n 1 - Doctors\n 2 - Facilities\n 3 - Laboratories \n 4 - Patients\n"))
    while selection != 0:
        if selection == 1:
            print("Doctors Menu")
            doctors_input = int(input(" 1 - Display Doctors List\n 2 - Search for Doctor by ID\n 3 - Search for doctor by name\n 4 - Add doctor\n 5 - Edit doctor info\n 6 - Back to Main Menu \n"))
        
                
            if doctors_input == 2:
                int(input("Enter the doctor ID:\n"))
                print("Back to previous menu")         

            if doctors_input == 3:
                input("Enter the doctors name\n")


            if doctors_input == 4:
                int(input("Enter the docotors ID \n"))

            if doctors_input == 5:
                int(input("Please enter the ID of the doctor that you want to edit their information: \n"))



        elif selection == 2:
            print("Select from the following options, or select 0 to stop:\n")
            facilties_input = int(input(" 1 - Display Facilities\n 2 - Add Facility\n 3 - Back to the main menu\n"))
            
            if facilties_input == 1:
                Facilities.displayFacilities(-1)
                
            if facilties_input == 2:
                Facilities.addFacility(-1)
        
        elif selection == 4:
           
            patients_input = int(input("\nPatients Menu:\n 1 - Display patients list\n 2 - Search for patient by ID\n 3 - Add patient\n 4 - Edit patient info\n 5 - Back to the Main Menu\n"))
            
            if patients_input == 1:
               
               Patients.displayPatientsInfo()
            if patients_input == 2:
                find_patient = Patients.readPatientsFile()
                Patients.searchPatientById(find_patient)


            if patients_input == 3:
                patient_info = Patients.readPatientsFile()
                add_patient = Patients.enterPatientInfo(patient_info)
                Patients.addPatientToFile(add_patient)

               



           
