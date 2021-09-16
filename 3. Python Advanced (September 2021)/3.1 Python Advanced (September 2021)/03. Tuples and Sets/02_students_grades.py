def average(values):
    return sum(values) / len(values)


students_cnt = int(input())
students = {}

for _ in range(students_cnt):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    average_grade = average(grades)
    grade_str = ' '.join([f"{x:.2f}" for x in grades])
    print(f"{student} -> {grade_str} (avg: {average_grade:.2f})")
