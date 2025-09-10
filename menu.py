#Inporting the student information 
def import_students(filename):
    #create an empy directory containing the student information
    studentInfo = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                #Remove new line characters and spaces
                line = line.strip()
                if line:
                #sID = studentID, sFirstName = student firstname, sLastName = student lastname, sMajor = student major, sGpa = student GPA 
                    sID, sLastName, sFirstName, sMajor, sGpa = line.split(",")
                    studentInfo[sID] = [sLastName, sFirstName, sMajor, sGpa]
    #If file doesen't exist
    except FileNotFoundError:
        print(f"File '{filename}' not found")

    return studentInfo

#displays the student information 
def display_studentInformation(sID, data):
    #varibles for the student information
    sLastName, sFirstName, sMajor, sGpa = data
    print(f"Student ID: {sID}, Student Last Name: {sLastName},Student First Name: {sFirstName}, Student Major: {sMajor}, Student GPA: {sGpa}")

#Function that will search for the students last name
def find_student_lastname(studentInfo):
    #Ask User for the last name 
    search_studentname = input("Please enter the last name for the student you are looking for: ").strip()
    detected = False
    #for loop for student to grab their information once their last name is searched
    for sID, data in studentInfo.items():
        if data[0].lower() == search_studentname.lower():
            display_studentInformation(sID,data)
            detected = True
    if not detected:
        print("The last name of the student you input is not found")

    
def find_student_major(studentInfo):
    search_major = input("Please enter the major of the student you are looking for: ")
    detected = False
    #grab the student information once the major is showed
    for sID, data in studentInfo.items():
        if data[2].lower() == search_major.lower():
            display_studentInformation(sID, data)
            detected = True
    if not detected:
        print("Major of the student not found")

    
def main ():
    #input the file name and the varible that is storing the dirctonary of student information
    filename = "student.txt"
    studentInformation = import_students(filename)
#Make a loop where the user is given a set of options and will loop until user exits
    while True:
        print( "Welcome, Please Choose One Of The Options Below :) ")
        print("1) Search by Last Name") 
        print("2) Seach by Major")
        print("3) Quit")
        print("---------------------------------")

        option = input("Please Enter Your Option: ").strip()

        if option == "1":
            find_student_lastname(studentInformation)
        elif option == "2":
            find_student_major(studentInformation)
        elif option == "3":
            print("Have a Great Day !!!")
            break 
        else:
            print("Please Choose One Of The Options Above ")

        

main()



     
        



