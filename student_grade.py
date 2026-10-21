name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

marks = []

for i in rahulrrrange(1, 4):
    while True:
        try:
            mark = float(input(f"Enter marks in Subject {i}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

average = sum(marks) / len(marks)

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

print("\n--- Student Result ---")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Average Marks:", round(average, 2))
print("Grade:", grade)