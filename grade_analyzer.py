student_list = [{"Name": "Ahmed", "Grade": 85}, {"Name": "Ali", "Grade": 92}, {"Name": "Sara", "Grade": 90}, {"Name": "John", "Grade": 88}]
grade_list = []


# Calculate the Average grade
for student in student_list:
    grade_list.append(student["Grade"])

average_grade = sum(grade_list) / len(grade_list)
    
print(f"Average Grade: {average_grade}")


# Find the Highest Grade
highest_grade = max(grade_list)
for student in student_list:
    if student["Grade"] == highest_grade:
        print(f"Highest Grade: {student['Name']} with {highest_grade}")

# Find the lowest grade
lowest_grade = min(grade_list)
for student in student_list:
    if student["Grade"] == lowest_grade:
        print(f"Lowest Grade: {student['Name']} with {lowest_grade}")

# Find students with a grade ≥ 85
for student in student_list:
    if student["Grade"]>= 85:
        print(f"Students with 85+:" , student["Name"], student["Grade"])



# Write a loop that goes through every student and prints their name and grade letter
for student in student_list:
    if student["Grade"] >= 90:
        grade_letter = "A"
    elif student["Grade"] >= 80:
        grade_letter = "B"
    elif student["Grade"] >= 70:
        grade_letter = "C"
    elif student["Grade"] >= 60:
        grade_letter = "D"
    else:
        grade_letter = "F"

    print(f" {student['Name']} has a grade letter of {grade_letter}")


# Check the performance of each student based on their grade letter

for student in student_list:
    if student["Grade"]>= 60:
        grade_performance = "Pass"
    else:
        grade_performance = "Fail"

    print(f"{student['Name']}: {grade_performance}")



# Using your student_list, write a program that:
# Goes through every student.
# Prints their name and grade.
# Prints "Pass" if their grade is 60 or higher, otherwise "Fail".
# At the end, prints the average grade of all students.
# You'll need to figure out how to keep track of the total grade while looping

total_grade = 0

for student in student_list:
    total_grade += student["Grade"]

average_grade = total_grade / len(student_list)

for student in student_list:
    if student["Grade"] >= 60:
        grade_performance = "Pass" 
    else:
        grade_performance = "Fail"

    print(f"{student['Name']} has a grade of {student['Grade']} and their performance is: {grade_performance}")


print(f"Total Grade: {total_grade}")
print(f"Average Grade: {average_grade}")