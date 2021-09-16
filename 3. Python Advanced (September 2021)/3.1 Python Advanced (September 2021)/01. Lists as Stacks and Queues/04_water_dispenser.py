from collections import deque

total_water = int(input())
people_queue = deque()

while True:
    command = input()

    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()

    if command == "End":
        break
    elif command.startswith('refill'):
        litters_to_add = int(command.split()[1])
        total_water += litters_to_add
    else:
        litters = int(command)

        if total_water - litters >= 0:
            total_water -= litters
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait")

print(f"{total_water} liters left")
