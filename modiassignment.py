students = ["arjun", "karan", "ravan", "krishna"]
subjects = ("Maths", "Physics", "Chemistry", "Computer Science")
marks = {"hanuman": 85,"shree ram": 92,"sita": 78,"lakshman": 88}
unique_values = (8.5, 9.2, 7.8, 8.8)

while True:
    print("\n1. Students")
    print("2. Subjects")
    print("3. Marks")
    print("4. Unique Values")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(students)
    elif choice == "2":
        print(subjects)
    elif choice == "3":
        print(marks)
    elif choice == "4":
        print(unique_values)
    elif choice == "5":
        break
    else:
        print("Wrong choice")
