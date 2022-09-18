number_of_students = int(input())

students_grades = {}

for _ in range(number_of_students):
    student_name, grade = input().split()

    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(float(grade))

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    all_grades = ' '.join(str(f"{grade:.2f}") for grade in grades)
    print(f"{student} -> {all_grades} (avg: {average_grade:.2f})")
