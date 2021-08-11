companies = {}
command = input()

while not command == "End":
    company, emp_id = command.split(" -> ")
    if company not in companies:
        companies[company] = [emp_id]
    else:
        if emp_id not in companies[company]:
            companies[company].append(emp_id)
    command = input()

for company, emp_ids in sorted(companies.items(), key=lambda kvp: kvp[0]):
    print(company)
    [print(f"-- {emp_id}") for emp_id in emp_ids]
