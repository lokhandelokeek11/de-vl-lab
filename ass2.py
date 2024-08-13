students = {}

def add_student_data():
    name = (input("Enter your name: "))
    score = int(input("Enter your marks: "))
    students[name] = {score}
    print(f"Added {name} with a score of {score}")
    
def update_score():
    name = input("Enter your name: ")
    if name in students:
        new_score = int(input("Enter new score: "))
        students[name] = new_score
        print(f"Updated score of {name} is {new_score}")
    else:
        print(f"{name} not found in the list...")
        
def delete_student_data():
    deleted_name = input("Enter the name you want to delete: ")
    if deleted_name in students: 
        del students[deleted_name]
        print(f"Deleted {deleted_name} from the list of students....")
    else:
        print(f"{deleted_name} not found in the list")
    
def highest_marks_students():
    if not students:
        print(f"No students found with the highst marks")
    else:
        highest_score = max(students.values())
        for name, score in students.items():
            if score == highest_score:
                print(f"Highest score is {highest_score} achived by {name}")
                
while True: 
    print(f"Student Data Management !!")
    print(f"1. Add Student Data")
    print(f"2. Update Score of Student ")
    print(f"3. Delete Student Data ")
    print(f"4. Find Highest Marks by a Student")
    print(f"5. Exit")
    
    choice = int(input("Enter your choice(1-5)"))
    
    if choice == "1": 
        add_student_data()
    if choice == "2": 
         update_score()
    if choice == "3": 
        delete_student_data()
    if choice == "4": 
        highest_marks_students()
    if choice == "5": 
         update_score()
        
                
    
    
students = {}

def add_student_data():
    name = (input("Enter your name: "))
    score = int(input("Enter your marks: "))
    students[name] = {score}
    print(f"Added {name} with a score of {score}")
    
def update_score():
    name = input("Enter your name: ")
    if name in students:
        new_score = int(input("Enter new score: "))
        students[name] = new_score
        print(f"Updated score of {name} is {new_score}")
    else:
        print(f"{name} not found in the list...")
        
def delete_student_data():
    deleted_name = input("Enter the name you want to delete: ")
    if deleted_name in students: 
        del students[deleted_name]
        print(f"Deleted {deleted_name} from the list of students....")
    else:
        print(f"{deleted_name} not found in the list")
    
def highest_marks_students():
    if not students:
        print(f"No students found with the highst marks")
    else:
        highest_score = max(students.values())
        for name, score in students.items():
            if score == highest_score:
                print(f"Highest score is {highest_score} achived by {name}")
                
while True: 
    print(f"Student Data Management !!")
    print(f"1. Add Student Data")
    print(f"2. Update Score of Student ")
    print(f"3. Delete Student Data ")
    print(f"4. Find Highest Marks by a Student")
    print(f"5. Exit")
    
    choice = int(input("Enter your choice(1-5)"))
    
    if choice == "1": 
        add_student_data()
    if choice == "2": 
         update_score()
    if choice == "3": 
        delete_student_data()
    if choice == "4": 
        highest_marks_students()
    if choice == "5": 
         update_score()
        
                
    
    
