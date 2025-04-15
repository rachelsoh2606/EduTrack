import os
#for assignment functions
from tkinter import filedialog
#for attendance functions
import random
from datetime import datetime, timedelta

#color formattings
bright_lime = '\033[1;92m'
bright_red = '\033[91m'
bright_white = '\033[97m'
light_green = '\033[92m'
light_yellow = '\033[93m'
light_cyan = '\033[96m'
aquamarine = '\033[96m'
purple = '\033[35m'
cyan = '\033[36m'
blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
bold = '\033[1m'
cyan_bold = "\033[1;36m"
yellow_bold = "\033[1;33m"  # Cyan color in bold
green_bold = '\033[1;32m'
red_bold = '\033[1;31m'
reset = "\033[0m"  # Reset color formatting

#assignment related functions
assignments = [] #List to store information of assignment in text file

#Allocate the text file assignment.txt to the identifier filepath
filepath = "assignments_StudentID.txt"

#This program check whether the text file exist or not.
#If the text file does not exist, it will prompt the users to check whether the text file enter is correct or not.
while True:
    try:
        if os.path.exists(filepath) == False:
            raise FileNotFoundError("File does not exist\nPlease check if you have enter the correct filepath")
    except FileNotFoundError as error:
        print(error)
    break
file = open(filepath,"r") #This code open the text file assignment.txt for reading
data = file.readlines() #This code read the assignment information in the text file and named it as data
file.close() #This function close the text file from reading
#This function(def read_assignment_from_file()) stores the assignment information into the list (assignment)
def read_assignment_from_file():
    for line in data:
        assignment_data = line.strip().split(',')
        assignment_info = {
                    'COURSE CODE': assignment_data[0],
                    'STUDENT ID': assignment_data[1],
                    'ASSIGNMENT NAME': assignment_data[2],
                    'STATUS': assignment_data[3]
                    }
        assignments.append(assignment_info)
def non_empty_input(prompt):
  while True:
      user_input = input(prompt)
      if user_input.strip(): # check if the input contains something other than blank
          return user_input
      else:
          print ("OOPS, looks like you didn't type anything. Please retype below")
def submit_assignment(self, selection, student_id, student_name, file_name):
    assignment_names = {
        "1": "CSC1024 PROGRAMMING PRINCIPLES",
        "2": "MPU3183_3112 PENGHAYATAN ETIKA DAN PERADABAN",
        "3": "MPU3193_3122 FALSAFAH DAN ISU SEMASA",
        "4": "MAT1024 LINEAR ALGEBRA & APPLICATIONS",
        "5": "NET1014 NETWORKING PRINCIPLES"
    }
    if selection in assignment_names:
        course_code, assignment_name = assignment_names[selection].split(maxsplit=1)
        if course_code not in self.assignments:
            self.assignments[course_code] = {}
        if student_id not in self.assignments[course_code]:
            self.assignments[course_code][student_id] = {}
        self.assignments[course_code][student_id][assignment_name] = "Submitted"

        print(f"Assignment '{assignment_name}' submitted successfully by student '{student_id}' for course '{course_code}'.")
    else:
        print("Invalid assignment selection.")

    #This function store the code for editing/updating assignment information
def update_assignment_info(assignment):
    print(f"Current Course Code: {assignment['COURSE CODE']}")
    choice_course_code = 'yes'
    while choice_course_code.lower()=='yes': #To check whether the user want to change the ISBN or not
        choice_course_code= non_empty_input("Do you want to enter a new course code? (yes/no): ")
        #If the user does not enter either yes or no, prompt the user to reenter yes or no only
        while choice_course_code.lower() != 'yes' and choice_course_code.lower() != 'no':
            choice_course_code = non_empty_input("Enter only yes or no: ")
        #If the user enter yes, prompt the user to change the assignment
        if choice_course_code.lower() == 'yes':
            new_course_code= non_empty_input("Enter a new Course Code:")
            #Print the new assignment
            assignment['COURSE CODE']= new_course_code
            print("Course Code updated successfully.")
            break
        #If the user enter no, inform user that the assignment remains unchanged
        if choice_course_code.lower() == 'no':
            print("Course Code remains unchanged")
            break   

    print(f"Current Student ID: {assignment['STUDENT ID']}")
    choice_student_id = 'yes'
    while choice_student_id.lower() == 'yes':#To check whether the user want to change the student ID or not
        choice_student_id= non_empty_input("Do you want to enter a new student id?(yes/no): ")
        #If the user does not enter either yes or no, prompt the user to reenter either yes or no only
        while choice_student_id.lower() != 'yes' and choice_student_id.lower() != 'no':
            choice_student_id = non_empty_input("Please enter yes or no only: ")
        #If the user enter yes, prompt the user to change the student id of the assignment
        if choice_student_id.lower() == 'yes':
            new_student_id=non_empty_input("Enter new student id: ")
            #Print the new student id of the assignment
            assignment['STUDENT ID'] = new_student_id
            print("Student ID updated successfully.")
            break
        #If the user enter no, inform the user that the Student remains unchanged
        if choice_student_id.lower() == 'no':
            print("Student ID remains unchanged.")
            break 

    print(f"Current Assignment Name: {assignment['ASSIGNMENT NAME']}")
    choice_assignment_name = 'yes'
    while choice_assignment_name.lower() == 'yes':#To check whether the user want change the title of the book or not
        choice_assignment_name = non_empty_input("Do you want to enter a new assignment name? (yes/no): ")
        #If the user does not enter either yes or no, prompt the user to reenter yes or no only
        while choice_assignment_name.lower() != 'yes' and choice_assignment_name.lower() != 'no':
            choice_assignment_name = non_empty_input("Please enter yes or no only: ")
        #If the user enter yes, prompt the user to change the title of the assignment
        if choice_assignment_name.lower() == 'yes':
            new_assignment_name = non_empty_input("Enter new assignment name: ")
            #Print the new name of the assignement
            assignment['ASSIGNMENT NAME'] = new_assignment_name
            print("Assignment Name updated successfully.")
            break
        #If the user enter no, inform the user that the assignment name remains unchanged
        if choice_assignment_name.lower() == 'no':
            print("Assignment Name remains unchanged.")
            break

    #Print the old status of the assignment               
    print(f"Current Status: {assignment['STATUS']}")
    choice_status = 'yes'
    while choice_status.lower() == 'yes': #To check whether the user want to change the status of the assignment or not
        choice_status = non_empty_input("Do you want to update the status? (yes/no): ")
        #If the user does not enter either yes or no, prompt the user to reenter either yes or no only
        while choice_status.lower() != 'yes' and choice_status.lower() != 'no':
            choice_status = non_empty_input("Please enter yes or no only: ")
        #If the user enter yes, prompt the user to change the status of the assignment
        if choice_status.lower() == 'yes':
            new_status = non_empty_input("Enter new status: ")
            #Print the new status of the assignment
            assignment['STATUS'] = new_status
            print("Status updated successfully.")
            break
        #If the user enter no, inform the user that the status remains unchanged
        if choice_status.lower() == 'no':
            print("Status remains unchanged.")
            break
def update_assignment():
  os.system('cls') #Clear the screen and run the program
  while True:
      #Prompt user to update the assignment info by either searching the course through the [1]Update by searching Course Code or [2]Update by searching Student ID and Assignment Name
      print(cyan_bold + "----"*15)
      print("Choose an option")
      print("1. Update by searching Course Code")
      print("2. Update by searching Student ID and Assignment Name")
      print(cyan_bold + "----"*15 + reset)
      choice= non_empty_input(yellow_bold + "Enter your choice: " + reset)

      #Match case for execute the function def update_book_code() to check if the user choose either option 1 or 2
      match choice.lower():
          case '1':
              Course_code_to_update = non_empty_input("Enter Course Code of the assignment to update: ")
              found = False
              #Loop all the assignment information in the list(assignment)
              for assignment in assignments:

                  #If the course code of the assignment match the course code entered, run the code in the function update_course_code()
                  if assignment['COURSE CODE'] == Course_code_to_update:

                      update_assignment_info(assignment)

                      found= True
                      print("Assignment updated successfully.")

              #If the course code is not found, inform the user that the assignment is not found and return to main page
              if not found:
                  print("Assignment not found...\nPlease try again.")
                  continue
              break

      # Write the changes back to the file
          case '2':
              student_id = non_empty_input ("Enter the Student ID:")
              assignment_name = non_empty_input ("Enter the assignment name:")
              found= False
              #Loop all the assignment information in the list(assignment)
              for assignment in assignments:
                  #If the Student ID and Assignment Name of the assignment match the course code entered, run the code in the function update_course_code()
                  if assignment['STUDENT ID'] == student_id and assignment['ASSIGNMENT NAME'] == assignment_name :

                      update_assignment_info(assignment)

                      found = True
                      print("Assignment updated successfully")
              #If the Student ID and Assignment Name are not found, inform the user that the assignment is not found and return to main page
              if not found:
                  print("Assignment not found...\nPlease try again.")
                  continue
              break
          #Inform the user that he/she enter the wrong input which is other than 1 or 2
          case _:
              print("Wrong input")
              continue

                #List for print the header of the table
information = ['COURSE CODE', 'STUDENT ID', 'ASSIGNMENT NAME', 'STATUS']
#This function store the code for displaying the assignment information if the assignment were read
#This function is used to display the all the assignments' information in table form
def display():
    os.system('cls') #Clear the screen and run the program
    print('-'*105)
    #Program for printing the header in eight column with spacing 20
    information = ["COURSE CODE", "STUDENT ID", "ASSIGNMENT NAME", "STATUS"]
    print(f"|{bold}{information[0]:^20}|{information[1]:^20}|{information[2]:^40}|{information[3]:^20}|{reset}")
    print("-"*105)
    #Loop for assignment information in the list(assignment)
    for assignment in assignments:
        status = assignment['STATUS'].strip().lower() #Extract the status of the assignment from the dictionary and lower case it
        course_code = assignment['COURSE CODE'][:17]
        student_id = assignment['STUDENT ID'][:15] 
        assignment_name = assignment['ASSIGNMENT NAME'][:35]
        print(f"|{course_code:^20}|{student_id:^20}|{assignment_name:^40}|{status:^20}|")
        print("-"*105)

#attendance related functions
#function to generate a check-in code for a lecture 
def generate_check_in_code(course_name, lecture_number):
    if lecture_number is None:
        print("Error: Lecture number not found for the selected course.")
        return
    #get current date with format dd/mm/yyyy
    cdate = datetime.now().strftime("%d/%m/%Y")
    #get current time with format hour:min:sec
    ctime = datetime.now().strftime('%H:%M:%S')
    #generate a random 5 digit code
    code = random.randint(10000, 99999)

    try:
        #open file in read & write mode
        with open("attendance_StudentID.txt", 'r+') as file:
            lines = file.readlines()

            #find the index of the course in the file
            course_index = None
            for i, line in enumerate(lines):
                if line.strip() == course_name:
                    course_index = i
                    break

            if course_index is not None:
                #find index of classes section
                classes_index = None
                for i, line in enumerate(lines[course_index:]):
                    if line.strip() == "Classes":
                        classes_index = course_index + i
                        break

                if classes_index is not None:
                    # insert new lecture after classes section
                    lines.insert(classes_index + 1, f"Lecture {lecture_number}\n")
                else:
                    print("Error: 'Classes' not found for the selected course.")

            else:
                #if course name not found, append it along with classes section and lecture number
                lines.append("\n" + course_name + "\nClasses\n")
                lines.append(f"Lecture {lecture_number}\n")

            #write updated lines to the textfile
            file.seek(0)
            file.writelines(lines)

        #display check-in code 
        print(f"Check-in code for {bold}{aquamarine}{course_name}{reset} Lecture {lecture_number} on {cdate}, {ctime}: {light_yellow}{code}")
        return code, datetime.now()

    except FileNotFoundError:
            print("Error: File 'attendance_StudentID.txt' not found.")
#function to display std name when user input std id
def search_student(file_path, student_id):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_index, line in enumerate(lines):
                if line.startswith(student_id + ":"):
                    #extract student name from the line e.g.: 123: Amirah to Amirah
                    student_name = line.split(":")[1].strip()  
                    print(f"Student name: {student_name}")
                    #if student found, return True, line index, and student name
                    return True, line_index, student_name  
            #if student not found, return False and None for line index and student name
            return False, None, None  

    except FileNotFoundError:
        return "File Not Found", None, None  
#function to let student checkin themselves using the checkin code
def check_in_student(file_path, line_index, check_in_code, check_in_time, student_name, lecture_number, course_name):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        #prompt for check-in code
        entered_code = input("Enter the check-in code: ")
        #check if code is correct
        if entered_code == str(check_in_code):
            #check if within 15 minutes
            if datetime.now() <= check_in_time + timedelta(minutes=15):
                #check if already checked in
                    if f"{student_name}: Lecture {lecture_number}\n" not in lines:
                        index = line_index + 1  
                        lines.insert(index, f"Lecture {lecture_number}\n")
                        print(f"{student_name} checked in for Lecture {lecture_number}.")
                    else:
                        print(f"{student_name} has already checked in for Lecture {lecture_number}.")
            else:
                print("The code is valid for 15 minutes only.")
        else:
            print("Error: The code is incorrect.")

        #save attendance data
        with open(file_path, 'w') as file:
            file.writelines(lines)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
#function to calculate student's attendance percentage
def calc_attendance(file_path, student_id):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            #call the search student function to get the student name
            found, line_index, student_name = search_student(file_path, student_id)
            if not found:
                return

            current_course = None
            control_lectures = {}
            total_classes = {}
            student_lectures = {}
            student_classes = {}
            attendance_percentage = {}
            current_student_section = False
            #count control_lectures (how many lectures are there)
            for line in lines:
                #remove leading and trailing whitespaces
                line = line.strip()  
                if line in ["CSC1024 PROGRAMMING PRINCIPLES",
                            "MPU 3183/MPU3112 PENGHAYATAN ETIKA DAN PERADABAN",
                            "MPU3193/3122 FALSAFAH DAN ISU SEMASA",
                            "MAT1024 LINEAR ALGEBRA & APPLICATIONS",
                            "NET1014 NETWORKING PRINCIPLES"]:
                    current_course = line
                    control_lectures[current_course] = []
                    total_classes[current_course] = 0
                elif current_course and line.startswith("Lecture "):
                    control_lectures[current_course].append(int(line.split()[-1]))
                    total_classes[current_course] += 1
                elif current_course and line == "":
                    current_course = None

            #count student_classes (how many classes std has attended)
            for line_index, line in enumerate(lines):
                line = line.strip()
                if line.startswith(student_id + ":"):
                    current_student_section = True
                    student_lectures[current_course] = []
                elif line in ["CSC1024 PROGRAMMING PRINCIPLES",
                                "MPU 3183/MPU3112 PENGHAYATAN ETIKA DAN PERADABAN",
                                "MPU3193/3122 FALSAFAH DAN ISU SEMASA",
                                "MAT1024 LINEAR ALGEBRA & APPLICATIONS",
                                "NET1014 NETWORKING PRINCIPLES"]:
                    current_course = line
                    student_classes[current_course] = []
                elif current_student_section and current_course:
                    if line.startswith("Lecture "):
                        student_classes[current_course].append(int(line.split()[-1]))
                    elif line:
                        lecture_number = int(line.split()[-1])
                        student_lectures[current_course].append(lecture_number)
                    else:
                        current_student_section = False

            #calculate attendance percentage for each course
            for course in control_lectures:
                control_total_classes = len(control_lectures[course])
                student_attended_lectures = set(student_classes.get(course, []))
                if control_total_classes > 0:
                    student_present_count = sum(lecture in student_attended_lectures for lecture in control_lectures[course])
                    attendance_percentage[course] = (student_present_count / control_total_classes) * 100

            #display the attendance percentage 
            for course in ["CSC1024 PROGRAMMING PRINCIPLES",
                            "MPU 3183/MPU3112 PENGHAYATAN ETIKA DAN PERADABAN",
                            "MPU3193/3122 FALSAFAH DAN ISU SEMASA",
                            "MAT1024 LINEAR ALGEBRA & APPLICATIONS",
                            "NET1014 NETWORKING PRINCIPLES"]:
                percentage = attendance_percentage.get(course, 0.0)
                classes_attended = len(student_classes.get(course, []))
                total_classes_count = len(control_lectures.get(course, []))
                print(f"{light_cyan}{course:<50}: {green_bold} {percentage:>6.2f}% {reset} (Attended {classes_attended} out of {total_classes_count} classes)")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
#function that holds the course menu (to choose which course)
def course_menu():
    while True:
        print(f"{cyan_bold}Select a course:{reset}")
        print("1. CSC1024 PROGRAMMING PRINCIPLES")
        print("2. MPU3183 PENGHAYATAN ETIKA DAN PERADABAN")
        print("3. MPU3193 FALSAFAH DAN ISU SEMASA")
        print("4. MAT1024 LINEAR ALGEBRA & APPLICATIONS")
        print("5. NET1014 NETWORKING PRINCIPLES")
        print(f"{bright_red}6. Exit{reset}")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"{bright_white}Course: CSC1024 PROGRAMMING PRINCIPLES")
            return "CSC1024 PROGRAMMING PRINCIPLES"
        elif choice == "2":
            print(f"{bright_white}Course: MPU3183 PENGHAYATAN ETIKA DAN PERADABAN")
            return "MPU 3183/MPU3112 PENGHAYATAN ETIKA DAN PERADABAN"
        elif choice == "3":
            print(f"{bright_white}Course: MPU3193 FALSAFAH DAN ISU SEMASA")
            return "MPU3193/3122 FALSAFAH DAN ISU SEMASA"
        elif choice == "4":
            print(f"{bright_white}Course: MAT1024 LINEAR ALGEBRA & APPLICATIONS")
            return "MAT1024 LINEAR ALGEBRA & APPLICATIONS"
        elif choice == "5":
            print(f"{bright_white}Course: NET1014 NETWORKING PRINCIPLES")
            return "NET1014 NETWORKING PRINCIPLES"
        elif choice == "6":
            raise ExitToMainMenu
        else:
            print("Invalid choice. Please try again.")

#timetable related function
class Timetable:
    def _init_(self, file_path=None):
        self.timetable = {}
        if file_path:
            self.load_timetable(file_path)

    # Loads timetable data from the textfile
    def load_timetable(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                day, start_time, course, instructor, room_no = data[0], data[1], data[2], data[3], data[4]
                self.create_timetable(day, start_time, course, instructor, room_no)

    # Method for user added into timetable
    def create_timetable(self, day, start_time, course, instructor, room_no):
        if day not in self.timetable:
            self.timetable[day] = {}

        # RANGE VALIDATION >> Check if the start time is within the specified range
        if not (800 <= int(start_time) <= 1800):
            print("\033[1;31mStart time must be between 0800 and 1800.\033[0m")
            return

        # SLOT ALIGNMENT >> Verifying that the start time aligns with a 2-hour slot
        if int(start_time) % 100 != 0:
            print("\033[1;31mStart time must be at the beginning of a 2-hour slot (e.g., 0800, 1000, 1200).\033[0m")
            return

        # TIMETABLE CONFLICT RESOLUTION >> Check for conflicts with existing for the specified day
        for existing_start_time, details in list(self.timetable[day].items()):
            existing_end_time = details['end_time']
            if int(start_time) < int(existing_end_time) and int(existing_start_time) < int(start_time):
                print("\033[1;33mThe time slot overlaps with an existing time slot. \033[0m")
                print(f"\033[1;33mCourse: {details['course']}, Instructor: {details['instructor']}, Room No: {details['room_no']}\033[0m")
                while True:
                    replace = input("Do you want to replace it? (YES/NO): ").strip().upper()
                    if replace in ("YES", "NO"):
                        break
                    else:
                        print("\033[1;31mInvalid Input. Please enter 'YES' or 'NO'.\033[0m")
                        continue

                if replace == "NO":
                    print("\033[1;31mTimetable entry not added.\033[0m")
                    return
                del self.timetable[day][existing_start_time]
                break  # Exit the loop after deleting the entry

        # CONFLICT CHECK >> Check for conflicts
        if start_time in self.timetable[day]:
            existing_entry = self.timetable[day][start_time]
            print("\033[1;33mA timetable entry already exists for the specified time:\033[0m")
            print(f"\033[1;33mCourse: {existing_entry['course']}, Instructor: {existing_entry['instructor']}, Room No: {existing_entry['room_no']}\033[0m")
            while True:
                replace = input("Do you want to replace it? (YES/NO): ").strip().upper()
                if replace in ("YES", "NO"):
                    break
                else:
                    print("\033[1;31mInvalid Input. Please enter 'YES' or 'NO'.\033[0m")
                    continue

            if replace == "NO":
                print("\033[1;31mTimetable entry not added.\033[0m")
                return

        end_time = self.calculate_end_time(start_time)
        self.timetable[day][start_time] = {
            'course': course,
            'instructor': instructor,
            'room_no': room_no,
            'end_time': end_time
        }

    # Method to print the timetable in a table format
    def display_timetable(self, day=None):
        print(f"{'-'*125}")
        print(f"{'Day':<10}  {'Time':<16}  {'Course':<55}  {'Instructor':<25}  {'Room No':<10}")
        print(f"{'-'*125}")

        if day is not None:
            found = False  # Variable keeps track of whether the timetable for the specified day is found
            if day in self.timetable:
                times = self.timetable[day]
                for start_time, details in times.items():
                    course = details['course']
                    instructor = details['instructor']
                    room_no = details['room_no']
                    end_time = details['end_time']
                    print(f"{day:<10}  {start_time} - {end_time:<10}  {course:<55}  {instructor:<25}  {room_no:<10}")
                    found = True
            if not found:
                print("\033[1;31mNo timetable available for the specified day.\033[0m")
        else:
            for day, times in self.timetable.items():
                for start_time, details in times.items():
                    course = details['course']
                    instructor = details['instructor']
                    room_no = details['room_no']
                    end_time = details['end_time']
                    print(f"{day:<10}  {start_time} - {end_time:<10}  {course:<55}  {instructor:<25}  {room_no:<10}")

        print(f"{'-'*125}")

    # Method to delete from the timetable
    def delete_timetable(self, day, start_time):
        while True:
            if day in self.timetable and start_time in self.timetable[day]:
                del self.timetable[day][start_time]
                print(f"\033[1;33mTimetable deleted for {day} at {start_time}\033[0m")
                break
            else:
                reenter = input("\033[1;33mTimetable not found.\033[0m \nDo you want to continue? (YES/NO): ").strip().upper()
                if reenter in ("YES", "NO"):  # Check if reenter is either "YES" or "NO"
                    if reenter == "YES":
                        start_time = input("Please enter a valid start time (e.g., 0800): ").strip()
                    else:
                        return  # If the user chooses not to continue, exit the function
                else:
                    print("\033[1;31mInvalid Input. Please enter 'YES' or 'NO'.\033[0m")

    # Method to update the timetable
    def update_timetable(self, day, start_time, new_course, new_instructor, new_room_no):
        while day in self.timetable and start_time not in self.timetable[day]:
            print("\033[1;33mTimetable entry not found for the specified day and start time.\033[0m")
            reenter = input("Do you want to re-enter the start time? (YES/NO): ").strip().upper()
            if reenter in ("YES", "NO"):  # Check if re-enter is either "YES" or "NO"
                if reenter == "YES":
                    start_time = input("Please enter a valid start time (e.g., 0800): ").strip()
                else:
                    return  # If the user chooses not to re-enter, exit the function
            else:
                print("\033[1;31mInvalid Input. Please enter 'YES' or 'NO'.\033[0m")
                continue

        if day in self.timetable and start_time in self.timetable[day]:
            if new_course and new_instructor and new_room_no:
                self.timetable[day][start_time]['course'] = new_course
                self.timetable[day][start_time]['instructor'] = new_instructor
                self.timetable[day][start_time]['room_no'] = new_room_no
                print(f"\033[1;33mTimetable updated for {day} at {start_time}: Course - {new_course}, Instructor - {new_instructor}, Room Number - {new_room_no}\033[0m")
        else:
            print("\033[1;31mTimetable not found in user input.\033[0m")

    # Calculate the end time of a class based on its start time
    @staticmethod
    def calculate_end_time(start_time):
        hours = int(start_time[:2])
        minutes = int(start_time[2:])
        end_hours = (hours + 2) % 24
        return f"{end_hours:02d}{minutes:02d}"

#function that holds the lecturer menu
def lecturer_menu():
    #declare variables as global
    global check_in_code, check_in_time  

    while True:
        choice = input(f"\n{cyan_bold}Select an option:{reset}\n{light_yellow}1. Generate check-in code\n2. View student's attendance percentage{reset}\n{red}3. Exit to main menu\n{reset}")
        #if user chooses to generate check-in code
        if choice == "1":
            course_name = course_menu()
            if course_name:
                lecture_number = input(f"{bright_lime}Enter current lecture number: {reset}")
                if not lecture_number.isdigit():
                    print(f"{bright_red}Error: Lecture number should be a valid integer.{reset}")
                    continue
                lecture_number = int(lecture_number)
                check_in_code, check_in_time = generate_check_in_code(course_name, lecture_number)
        #if user chooses to view student's attendance percentage
        elif choice == "2":
            student_id = input("Enter student ID: ")
            calc_attendance("attendance_StudentID.txt", student_id)  
        #if user chooses to exit to main menu (to choose to enter as lecturer or student)
        elif choice == "3":
            raise ExitToMainMenu
        else:
            print(f"{red_bold}Invalid choice. Please try again.{reset}")
check_in_code, check_in_time = None, None
#hold the student function menu
def student_function_menu():
    while True:
        print(f"{cyan_bold}\nStudent Menu{reset}\n{bright_lime}1. Submit/Check Assignments\n2. Mark Attendance\n3. Manage Timetable\n4. Display{reset}\n{bright_red}5. Exit{reset}")
        function_choice = input("Enter your choice: ")

        if function_choice == "1":
            #call the function to view assignments
            read_assignment_from_file()

            while True:
                print(f"{cyan_bold}{'Assignment Tracking System:'}{reset}")
                print(f"{blue}{'1. Submit Assignment'}{reset}")
                print(f"{blue}{'2. Check Assignment Status'}{reset}")
                print(f"{blue}{'3. Update Assignment Status (Faculty)'}{reset}")
                print(f"{blue}{'4. Exit'}{reset}")
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("[1]CSC1024 PROGRAMMING PRINCIPLES")
                    print("[2]MPU3183_3112 PENGHAYATAN ETIKA DAN PERADABAN")
                    print("[3]MPU3193_3122 FALSAFAH DAN ISU SEMASA")
                    print("[4]MAT1024 LINEAR ALGEBRA & APPLICATIONS")
                    print("[5]NET1014 NETWORKING PRINCIPLES")
                    selection = input("Which assignment do you want to submit: ")
                    student_id = input("Enter your student ID: ")
                    student_name = input("Enter your name: ")
                    print("Please select a PDF file to upload:")
                    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
                    if filename:
                        print("Selected file:", filename)
                    else:
                        print("No file selected.")

                    confirmation = input(f"Do you want to submit the file '{filename}'? (yes/no): ")
                    if confirmation.lower() == 'yes':
                        print("File submitted successfully.")
                        
                    else:
                        print("Submission canceled.")
                elif choice == "2":
                    display()
                elif choice == "3":
                  faculty_password = input("Enter faculty password: ")
                  # Add authentication mechanism here
                  if faculty_password == "123123":
                    update_assignment()
                    
                  else:
                    print("Incorrect password. Access denied.")

                elif choice == "4":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

                input("\n" + "Press Enter to return to main page")


        elif function_choice == "2":
            #call all attendance related functions
            global check_in_code, check_in_time

            if check_in_code is None or check_in_time is None:
                print(f"{red_bold}No check-in code has been generated yet.{reset}")
                continue
            else:
                while True:
                    student_id = input("Enter your student ID: ")
                    found, line_index, student_name = search_student("attendance_StudentID.txt", student_id)
                    if found == "File Not Found":
                        print(f"{red_bold}Error: File 'attendance_StudentID.txt' not found.{reset}")
                        continue
                    elif found:
                        while True:
                            choice = input(f"{green_bold}Select an option:{reset}\n{aquamarine}{bold}1. Check in\n2. Your attendance percentage{reset}\n{bright_red}3. Exit to student menu{reset}\n")
                            if choice == "1":
                                selected_course = course_menu()
                                lecture_number = input("Enter current lecture number: ")
                                if not lecture_number.isdigit():
                                    print(f"{red_bold}Error: Lecture number should be a valid integer.{reset}")
                                    continue
                                lecture_number = int(lecture_number)
                                check_in_student("attendance_StudentID.txt", line_index, check_in_code, check_in_time, student_name, lecture_number, selected_course)
                            elif choice == "2":
                                calc_attendance("attendance_StudentID.txt", student_id)
                            elif choice == "3":
                                inner_loop_broken = True  #setting to True, indicating that inner loop is broken
                                break
                            else:
                                print(f"{red_bold}Invalid choice. Please try again.{reset}")
                        if inner_loop_broken:
                            break
                    else:
                        print(f"{red_bold}Student ID '{student_id}' not found in the file.{reset}")
                        continue

        elif function_choice == "3":
            # Define the file path where the timetable data is stored
            file_path = "timetables_StudentID.txt"
            timetable_manager = Timetable(file_path)
            timetable_manager.display_timetable()

            while True:
                # Display the menu option for user
                print("\nSelect an option:")
                print("1. Create Timetable")
                print("2. Update Timetable")
                print("3. Delete Timetable")
                print("4. Display Timetable")
                print("5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    # Create Day
                    while True:
                        day = input("Enter day(e.g., \033[1;32mMONDAY\033[0m): ").upper()
                        if day.strip() in ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"): 
                            break 
                        elif day.strip() == "":
                            print("\033[1;31mDay cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input\033[0m")
                    # Create Start Time           
                    while True:
                        start_time = input("Enter start time (e.g., \033[1;32m0800\033[0m): ")
                        if start_time.strip().isdigit() and (800 <= int(start_time) <= 1800):
                            break
                        elif start_time.strip() == "":
                            print("\033[1;31mStart time cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input. Start time must be between 0800 and 1800.\033[0m")           
                    # Create Course
                    while True:
                        course = input("Enter course (e.g., \033[1;32mCSC1024 PROGRAMMING PRINCIPLES\033[0m): ").upper()
                        if course.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")
                    # Create Instructor
                    while True:
                        instructor = input("Enter instructor (e.g., \033[1;32mDR EMILY CHANG\033[0m): ").upper()
                        if instructor.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")           
                    # Create Room Number
                    while True:
                        room_no = input("Enter room number (e.g., \033[1;32mROOM 100\033[0m): ").upper()
                        if room_no.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")
                    timetable_manager.create_timetable(day, start_time, course, instructor, room_no)
                    timetable_manager.display_timetable()

                elif choice == "2":
                    # Update Day
                    while True:
                        day = input("Enter the day you wish to update (e.g., \033[1;32mMONDAY\033[0m): ").upper()
                        if day.strip() in ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"): 
                            break 
                        elif day.strip() == "":
                            print("\033[1;31mDay cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input\033[0m")           
                    # Update Start Time
                    while True:
                        start_time = input("Enter the start time of the day you wish to update (e.g., \033[1;32m0800\033[0m): ")
                        if start_time.strip().isdigit() and (800 <= int(start_time) <= 1800):
                            break
                        elif start_time.strip() == "":
                            print("\033[1;31mStart time cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input. Start time must be between 0800 and 1800.\033[0m")           
                    # Update Course
                    while True:          
                        new_course = input("Enter the new course you wish to update (e.g., \033[1;32mCSC1024 PROGRAMMING PRINCIPLES\033[0m): ").upper()
                        if new_course.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")        
                    # Update Instructor
                    while True:
                        new_instructor = input("Enter the new instructor you wish to update (e.g., \033[1;32mDR EMILY CHANG\033[0m): ").upper()
                        if new_instructor.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")
                    # Update Room Number
                    while True:  
                        new_room_no = input("Enter the new room number you wish to update (e.g., \033[1;32mROOM 100\033[0m): ").upper()
                        if new_room_no.strip() != "":
                            break
                        else:
                            print("\033[1;31mInvalid Input\033[0m")
                    timetable_manager.update_timetable(day, start_time, new_course, new_instructor, new_room_no)
                    timetable_manager.display_timetable()


                elif choice == "3":
                    # Delete Day
                    while True:
                        day = input("Enter the day you wish to delete (e.g., \033[1;32mMONDAY\033[0m): ").upper()
                        if day.strip() in ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"): 
                            break 
                        elif day.strip() == "":
                            print("\033[1;31mDay cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input\033[0m")           
                    # Delete Start Time
                    while True:
                        start_time = input("Enter start time of the day you wish to delete (e.g., \033[1;32m0800\033[0m): ")
                        if start_time.strip().isdigit() and (800 <= int(start_time) <= 1800):
                            break
                        elif start_time.strip() == "":
                            print("\033[1;31mStart time cannot be empty\033[0m")
                        else:
                            print("\033[1;31mInvalid Input. Start time must be between 0800 and 1800.\033[0m")       
                    timetable_manager.delete_timetable(day, start_time)
                    timetable_manager.display_timetable()

                elif choice == "4":
                    while True:
                        day = input("Enter day to display (enter \033[1;32mALL\033[0m for all days): ").upper()
                        if day == "ALL":
                            timetable_manager.display_timetable()
                            break
                        elif day.strip() == "":
                            print("\033[1;31mDay cannot be empty\033[0m")
                        else:
                            timetable_manager.display_timetable(day)
                            break

                elif choice == "5":
                    print("Exiting...")
                    break

                else:
                    print("Invalid Choice. Please enter a number between 1 and 5.")

        elif function_choice == "4":

            while True:
                print("\nMenu:")
                print("1. Display Assignment Status")
                print("2. Display Attendance Percentage")
                print("3. Display Timetable")
                print("4. Exit to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    display()
                elif choice == "2":
                    student_id = input("Enter your student ID: ")
                    found, line_index, student_name = search_student("attendance_StudentID.txt", student_id)
                    if found == "File Not Found":
                        print(f"{red_bold}Error: File 'attendance_StudentID.txt' not found.{reset}")
                        continue
                    elif found:
                        calc_attendance("attendance_StudentID.txt", student_id)
                elif choice == "3":
                    # Define the file path where the timetable data is stored
                    file_path = "timetables_StudentID.txt"
                    timetable_manager = Timetable(file_path)
                    while True:
                        day = input("Enter day to display (enter \033[1;32mALL\033[0m for all days): ").upper()
                        if day == "ALL":
                            timetable_manager.display_timetable()
                            break
                        elif day.strip() == "":
                            print("\033[1;31mDay cannot be empty\033[0m")
                        else:
                            timetable_manager.display_timetable(day)
                            break
                elif choice == "4":
                   break
                else:
                    print("Invalid choice. Please try again.")
        elif function_choice == "5":
            # Exit to the main menu
            break
        else:
            print("Invalid choice. Please try again.")

#custom exception to exit to main menu
class ExitToMainMenu(Exception):
    pass
#Main program
if __name__ == "_main_":
    file_path = "attendance_StudentID.txt"

    while True:
        choice = input(f"\n{light_yellow}Are you a {cyan_bold}lecturer{reset} {light_yellow}or a {reset} {purple}student? {reset} \n{light_green}Select an option: {reset} \n{cyan_bold}1. Lecturer{reset} \n{purple}2. Student {reset}\n{red}3. Quit {reset}\n")

        #if user chooses to enter as lecturer
        if choice == "1":
            try:
                lecturer_menu()
            except ExitToMainMenu:
                continue
        #if user chooses to enter as student
        elif choice == "2":
            try:
                student_function_menu()  
            except ExitToMainMenu:
                continue
        #if user chooses to quit - stop the program
        elif choice == "3":
            break
        else:
            print("Invalid user type.")