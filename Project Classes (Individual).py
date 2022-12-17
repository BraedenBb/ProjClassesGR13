# Project Classes (Laboratories Class)
# Author: Angelo De Guzman
# Version 1.4
####################################################
# Laboratories
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
            print("\nDoctors are not avaliable in this version of the code. Please select Laboratories for this file.\n"); break
        
        if Selection == 2:
            print("\nFacilities are not avaliable in this version of the code. Please select Laboratories for this file.\n"); break
        
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
            print("Patients are not avaliable in this version of the code. Please select Laboratories for this file.\n"); break

    if Selection == 0: 
        print("Thank you for using the Alberta Hospital Management System."); exit()

    Selection = int(input("1: Doctors \n2: Facilities \n3: Laboratories \n4: Patients \n0: Stop\n"))
    
    if Selection == 0: 
        print("Thank you for using the Alberta Hospital Management System."); exit()