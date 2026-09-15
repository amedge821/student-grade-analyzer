student_list = [{"Name": "Ahmed", "Grade": 85}, {"Name": "Ali", "Grade": 92}, {"Name": "Sara", "Grade": 78}]


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
