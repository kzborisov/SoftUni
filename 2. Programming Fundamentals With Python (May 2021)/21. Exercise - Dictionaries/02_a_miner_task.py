command = input()
resources = {}

while not command == "stop":
    qty = int(input())
    if command not in resources:
        resources[command] = qty
    else:
        resources[command] += qty
    command = input()

for k, v in resources.items():
    print(f"{k} -> {v}")
