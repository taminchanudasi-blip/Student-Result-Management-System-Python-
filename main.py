import csv

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    m1 = int(input("Enter Marks of Subject 1: "))
    m2 = int(input("Enter Marks of Subject 2: "))
    m3 = int(input("Enter Marks of Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3
    grade = calculate_grade(percentage)

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, m1, m2, m3, total, percentage, grade])

    print("Student Record Saved Successfully!")

def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
