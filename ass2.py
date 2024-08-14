students = {}

def add_student_data():
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students[name] = score
    print(f"Added {name} with a score of {score}")

def update_score():
    name = input("Enter student name: ")
    if name in students:
        new_score = int(input("Enter new score: "))
        students[name] = new_score
        print(f"Updated {name}'s score to {new_score}")
    else:
        print(f"{name} not found in the list of students.")

def deleted_student_data():
    name = input("Enter student name you want to delete: ")
    if name in students:
        del students[name]
        print(f"Deleted {name} from the list of students.")
    else:
        print(f"{name} not found in the list of students.")

def highest_marks_student():
    if not students:
        print("No students found with highest marks.")
    else:
        highest_score = max(students.values())
        for name, score in students.items():
            if score == highest_score:
                print(f"Highest score: {score} (Student: {name})")

def display_students():
    if not students:
        print("No students found.")
    else:
        print("Students and their scores:")
        for name, score in students.items():
            print(f"{name}: {score}")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Score")
    print("3. Delete Student")
    print("4. Find Highest Score")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student_data()
    elif choice == "2":
        update_score()
    elif choice == "3":
        deleted_student_data()
    elif choice == "4":
        highest_marks_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        print("Exiting Student Management System...")
        break
    else:
        print("Invalid choice. Please try again.")
