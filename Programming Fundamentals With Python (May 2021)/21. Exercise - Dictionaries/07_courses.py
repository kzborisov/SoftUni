courses = {}  # -> name: [student1, student 2]

command = input()

while not command == "end":
    course, student_name = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student_name)
    command = input()

for course, students in sorted(courses.items(), key=lambda kvp: -len(kvp[1])):
    print(f"{course}: {len(students)}")
    [print(f"-- {student}") for student in sorted(students)]

