# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
# James Connolly,11/10/2026,Created Script
# ------------------------------------------------------------------------------------------ #

# Import the required modules
import json
# Define the data constants
FILE_NAME: str = 'MyLabData.json'
MENU: str = '''
---- Student GPAs ------------------------------
 Select from the following menu:
 1. Show current student data.
 2. Enter new student data.
 3. Save data to a file.
 4. Exit the program.
--------------------------------------------------
'''

# Define the program's data
student_first_name: str = '' # Holds the first name of a student
student_last_name: str = '' # Holds the last name of a student
student_gpa: float = 0.0 # Holds the GPA of a student
message: str = '' # Holds a custom message string
menu_choice: str = '' # Hold the choice made by the user
student_data: dict = {} # one row of student data
students: list = [] # a table of student data
file_data: str = '' # Holds combined string data separated by a comma
file = None # Not using type hint helps PyCharm, we won't use it going forward

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
# Transform the data from the file
# Load it into the collection
#file = open(FILE_NAME, "r")
#for row in file.readlines():
#    student_data = row.split(',')
#    student_data = {"FirstName": student_data[0],
#                    "LastName": student_data[1],
#                    "GPA": float(student_data[2].strip())}
#    students.append(student_data)
#file.close()
file = open(FILE_NAME, "r")
students = json.load(file)
file.close()
# Repeat the follow tasks
# display the table's current data
# Add data to the table
# Save the data to the file
# Exit the program
while True:
    print(MENU)
    menu_choice = input('Enter your menu choice number: ')
    print() # Adding extra space to make it look nicer
    if menu_choice == '1':
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue
    elif menu_choice == '2':
        student_first_name = input('What is the student\'s first name? ')
        student_last_name = input('What is the student\'s last name? ')
        student_gpa = float(input('What is the student\'s GPA? '))
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
        continue
    elif menu_choice == '3':
    #    file = open(FILE_NAME, "w")
    #    for student in students:
    #        file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
    #    file.close()
    #    print("Data Saved!")
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        continue
    elif menu_choice == '4':
        break