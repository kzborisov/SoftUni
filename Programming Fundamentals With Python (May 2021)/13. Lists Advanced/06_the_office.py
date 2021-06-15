# Task 06. The Office
def average(lst):
    return sum(lst) / len(lst)


employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

employees_happiness = [x * improvement_factor for x in employees_happiness]
happy = [x for x in employees_happiness if x >= average(employees_happiness)]

print(f"Score: {len(happy)}/{len(employees_happiness)}.", end=" ")
if len(happy) >= len(employees_happiness) // 2:
    print("Employees are happy!")
else:
    print("Employees are not happy!")
