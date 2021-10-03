from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    elif female <= 0:
        females.popleft()
        continue
    elif male % 25 == 0:
        males.pop()
        continue
    elif female % 25 == 0:
        females.popleft()
        continue
    elif male == female:
        females.popleft()
        males.pop()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
