from collections import deque

people_deque = deque(input().split())
step = int(input())

while people_deque:
    for _ in range(step - 1):
        people_deque.append(people_deque.popleft())
    potato_to_remove = people_deque.popleft()

    if people_deque:
        print(f"Removed {potato_to_remove}")
    else:
        print(f"Last is {potato_to_remove}")
