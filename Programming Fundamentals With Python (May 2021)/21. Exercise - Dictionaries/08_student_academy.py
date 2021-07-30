def average(lst):
    return sum(lst) / len(lst)


def filter_grades(grades_dict):
    filtered = grades_dict.copy()
    for student_name, student_grades in grades_dict.items():
        average_grade = average(student_grades)

        if average_grade < 4.5:
            filtered.pop(student_name)
    return filtered


grades = {}
n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

filtered_dict = filter_grades(grades)

for k, v in sorted(filtered_dict.items(), key=lambda kvp: -average(kvp[1])):
    print(f"{k} -> {average(v):.2f}")
