emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
questions = int(input())

total_people_per_hour = emp_1 + emp_2 + emp_3
hours = 0

while questions > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    questions -= total_people_per_hour

print(f"Time needed: {hours}h.")
