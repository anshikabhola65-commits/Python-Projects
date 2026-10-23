student = {}

while True:
    print("/n -----STUDENT MANAGER APP-----")
    print("1. Add student")
    print("2. View all student")
    print("3. Check result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter your name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully added!")


    # view student
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":" , marks)

    # Check result
    elif choice == "3":
        name = input("Enter Student name: ")

        if name in student :
            marks = student[name]

            if marks >= 40 :
               print("PASS")
            else:
                print("FAIL")
        else:
           print("Student not found!")    

    # Exit
    elif choice == "4":
        print("Exiting.....")
        break

    else:
        print("In-Valid input")    