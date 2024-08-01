def calculate_grade_and_average(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return average, grade

marks = [85, 92, 78, 88,]
average, grade = calculate_grade_and_average(marks)
print(f"Average Marks: {average}, Grade: {grade}")
