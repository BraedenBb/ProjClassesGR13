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
    if doctors==5:
        break  
    print("Doctors Menu:\n 1 - Display Doctors list\n 2 - Search for doctor by ID\n 3 - Search for doctor by name\n 4 - Add doctor\n 5 - Edit doctor info\n 6 - Back to the Main Menu\n")
    doctors=int(input())
