print("\nWelcome to Alberta Hospital (AH) Management system\n")

class Doctors:
#Constructor#
    def __init__(self, id, name, special, qual, roomnum):
        self.id = id
        self.name = name
        self.special = special
        self.qual = qual
        self.roomnum = roomnum









class Management:
    selection = int(input("Select from the following options, or select 0 to stop\n 1 - Doctors\n 2 - Facilities\n 3 - Laboratories \n 4 - Patients\n"))
    if selection == 1:
        print("Doctors Menu")
        int(input(" 1 - Display Doctors List\n 2 - Search for Doctor by ID\n 3 - Search for doctor by name\n 4 - Add doctor\n 5 - Edit doctor info\n 6 - Back to Main Menu \n"))
        
        if selection == 1:
            print
        
        if selection == 2:
            int(input("Enter the doctor ID:\n"))
            print("Back to previous menu")
                

                    

        if selection == 3:
            input("Enter the doctors name\n")


        if selection == 4:
            int(input("Enter the docotors ID \n"))
            input("Enter the doctors name\n")  
            input("Enter the doctors speciality\n") 
            input("Enter the docotor's timing (e.g., 7am-10pm)")
            input ("Enter the docots qualification\n")
            int(input("Enter the doctor's room number"))

        if selection == 5:
            int(input("Please enter the ID of the doctor that you want to edit their information: \n"))




    elif selection == 2:



    elif selection == 3:
        

