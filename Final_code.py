import csv
from tabulate import tabulate
class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    @classmethod
    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID: ")
        self.name = input("Enter the doctor's name: ")
        self.specialization = input("Enter the doctor's specialization: ")
        self.working_time = input("Enter the doctor's working time: ")
        self.qualification = input("Enter the doctor's qualification: ")
        self.room_number = input("Enter the doctor's room number: ")
        info_list=[self.id,self.name,self.specialization,self.working_time,self.qualification,self.room_number]
        info_list.insert(1,'_')
        info_list.insert(3,"_")
        info_list.insert(5,"_")
        info_list.insert(7,"_")
        info_list.insert(9,"_")
        res=''.join([str(item)for item in info_list])
        return res
    def addDrToFile(info):
        with open('doctors.txt','a') as f:
            f.write(f'\n{info}')
    def editDoctorInfo(doc_list,old_info):
        templist=doc_list
        new_list=[item for item in templist if any(x not in (old_info) for x in item)]
        templist2=new_list
        return templist2
    def writeListOfDoctorsToFile(new_list):
        file=open('doctors.txt','w',newline='')
        with file:
            write=csv.writer(file)
            write.writerows(new_list)
    @staticmethod
    def readDoctorsFile():
        doctors = []
        openfile=open("doctors.txt", 'r')
        DrFile=openfile.readlines()
        for line in DrFile:
            doctors.append(line.strip())
        for x in range(len(doctors)):
            doc_list.append(doctors[x].split("_"))

        return doc_list
    def searchDoctorById(doc_list):
        tempID=input(f" Please enter the doctor's ID:")
        for x in range(len(doc_list)):
            if doc_list[x][0]==tempID:
              return doc_list[x]
            if tempID!=doc_list:
                print("Can't find the doctor with the same ID on the system")
    def searchDoctorByName(doc_list):
        tempName=input(f"Please enter the doctor's Name: ")
        for x in range(len(doc_list)):
            if tempName in doc_list[x][1]:
                return doc_list[x]
            if tempName not in doc_list[x][1]:
                print(f"Can't find the doctor with the same Name on the system")
                pass
        return
    def displayDoctorInfo1():
        doc_list.pop(0)
        head = ["ID", "Name", "Specialty", "Timing", "Qualifications", "Room Number"]
        print (tabulate(doc_list, headers=head, tablefmt="fancy_grid"))
    def displayDoctorInfo2(doc_list):
        head = ["ID", "Name", "Specialty", "Timing", "Qualifications", "Room Number"]
        print (tabulate([doc_list], headers=head, tablefmt="fancy_grid"))

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
        self.pid = int(input("Enter Patient ID:"))
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
lab_list = []
class Laboratories:

    def __init__(self, name, cost): 
        self.name = name
        self.cost = cost

    @staticmethod
    def readLaboratoryFile():
        labs = []
        openfile = open("laboratories.txt", 'r')
        labfile = openfile.readlines()
        for line in labfile:
            labs.append(line.strip())

        for x in range(len(labs)):

            lab_list.append(labs[x].split("_"))
        return lab_list 

    @classmethod
    def enterLaboratoryInfo(self):
        self.name = input("Enter the name of the Laboratory: ")
        self.cost = input("Enter the cost of the Laboratory: ")
        info_list = [self.name,self.cost]
        info_list.insert(1," | ")
        res = ''.join([str(item) for item in info_list])
        return res

    def writeListOfLabsToFile(self):
        self.lab_list = Laboratories
        wfile = open("laboratories.txt", 'w')
        for y in range(len(Laboratories.lab_list)):
            wfile.write(self.lab_list)

    def addLabToFile(info):
        with open('laboratories.txt', 'a') as f:
            f.write(f'\n{info}')

    def formatLabInfo(self):
        return f"{self.name}_{self.cost}"
        
    def displayLaboratoryInfo():
        print()
        file = open("laboratories.txt", 'r')
        print(file.read(-1))

print("Welcome to the Alberta Hospital Management System. \nPlease select from the following:\n==========================================================")
class Management:
    Selection = int(input("1: Doctors \n2: Facilities \n3: Laboratories \n4: Patients \n0: Stop\n"))

    while Selection > 3 or Selection < 0:
        print("\nError: Invalid Selection.\nTry Again.")
        Selection = int(input("==========================================================\n1: Doctors \n2: Facilities \n3: Laboratories \n4: Patients \n0: Stop\n"))
    
    while Selection != 0:

        if Selection == 1:
            print("Doctors Menu:\n 1 - Display Doctors list\n 2 - Search for doctor by ID\n 3 - Search for doctor by name\n 4 - Add doctor\n 5 - Edit doctor info\n 6 - Back to the Main Menu\n")

            doctors=int(input())
            while doctors > 0:
                doc_list=[]
                if doctors==1:
                    doc_list=Doctor.readDoctorsFile()
                    Doctor.displayDoctorInfo1()
    
                if doctors==2:
                    doc_list=Doctor.readDoctorsFile()
                    tes=Doctor.searchDoctorById(doc_list)
                if tes==None:
                    pass
                else:
                    Doctor.displayDoctorInfo2(tes)
    
                if doctors==3:
                    doc_list=Doctor.readDoctorsFile()
                    test=Doctor.searchDoctorByName(doc_list)
                if test==None:
                    pass
                else:
                    Doctor.displayDoctorInfo2(test)

                if doctors==4:
                    new_dr=Doctor.enterDrInfo()
                    Doctor.addDrToFile(new_dr)
                if doctors==5:
                    doc_list=Doctor.readDoctorsFile()
                    old_info=Doctor.searchDoctorById(doc_list)
                    new_info=Doctor.enterDrInfo()
                    new_list=Doctor.editDoctorInfo(doc_list,old_info)
                    Doctor.writeListOfDoctorsToFile(new_list)
                    Doctor.addDrToFile(new_info)
                    pass
                if doctors==6:
                    break  
                print("Doctors Menu:\n 1 - Display Doctors list\n 2 - Search for doctor by ID\n 3 - Search for doctor by name\n 4 - Add doctor\n 5 - Edit doctor info\n 6 - Back to the Main Menu\n")
                doctors=int(input())
        
        if Selection == 2:
            print("Select from the following options, or select 0 to stop:\n")
            facilties_input = int(input(" 1 - Display Facilities\n 2 - Add Facility\n 3 - Back to the main menu\n"))
            
            if facilties_input == 1:
                Facilities.displayFacilities(-1)
                
            if facilties_input == 2:
                Facilities.addFacility(-1)
        
        if Selection == 3:
            print("\nLaboratories \n==========================================================")
            lab_choice = int(input("1: Display laboratories list \n2: Add Laboratory \n3: Return to main menu \n"))
            
            while lab_choice > 3 or lab_choice < 0:
                print("\nError: Invalid Selection.\nTry Again.")
                lab_choice = int(input("1: Display laboratories list \n2: Add Laboratory \n3: Return to main menu \n"))
            
            if lab_choice == 1:
            
                Laboratories.displayLaboratoryInfo()
            if lab_choice == 2:
                newlab = Laboratories.enterLaboratoryInfo()
                Laboratories.addLabToFile(newlab)
            
            if lab_choice == 3:
                print("\nReturning to Main Menu...\n=========================================================="); break
        
        if Selection == 4:
           
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


    if Selection == 0: 
        print("Thank you for using the Alberta Hospital Management System."); exit()

    Selection = int(input("1: Doctors \n2: Facilities \n3: Laboratories \n4: Patients \n0: Stop\n"))
    
    if Selection == 0: 
        print("Thank you for using the Alberta Hospital Management System."); exit()