from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
target_index = int(input())

threshold = jobs[target_index]
cycles = 0

while jobs:
    job = jobs.popleft()
    if job <= threshold:
        cycles += job

print(cycles)
