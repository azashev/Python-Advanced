n = int(input())

students = {}

for _ in range(n):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for data in students.items():
    print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})")


# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in
# the format:
# {student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})
#
# The order in which we print the result does not matter.
