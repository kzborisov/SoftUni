from collections import deque

people_queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(people_queue)} people remaining.")
        break
    elif command == "Paid":
        while people_queue:
            print(people_queue.popleft())
    else:
        people_queue.append(command)
