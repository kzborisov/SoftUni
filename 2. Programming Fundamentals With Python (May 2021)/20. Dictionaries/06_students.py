# Task 06 Students
student = input()
students = {}

while ":" in student:
    student_info = student.split(":")
    student_name = student_info[0]
    students[student_name] = student_info[1:]

    student = input()


final_course = student.replace('_', " ")
for student in students:
    if final_course in students[student]:
        print(f"{student} - {students[student][0]}")
