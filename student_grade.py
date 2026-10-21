name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

print("\nEnter marks out of 100")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

if all(0 <= m <= 100 for m in [m1, m2, m3]):

    average = (m1 + m2 + m3) / 3

    if average >= 90:
        grade = "S"
    elif average >= 80:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n===== STUDENT DETAILS =====")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Subject 1 Marks:", m1)
    print("Subject 2 Marks:", m2)
    print("Subject 3 Marks:", m3)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)

else:
    print("Invalid marks! Enter marks between 0 and 100.")