from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0


def print_result(matches, males, females):
    print(f"Matches: {matches}")
    if not males:
        print("Males left: none")
    else:
        print(f"Males left: {', '.join(reversed([str(x) for x in males]))}")

    if not females:
        print("Females left: none")
    else:
        print(f"Females left: {', '.join(str(x) for x in females)}")


while males and females:
    if males[-1] <= 0:
        males.pop()
        continue

    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        for _ in range(2):
            males.pop()
        continue

    if females[0] % 25 == 0:
        for _ in range(2):
            females.popleft()
        continue

    male = males.pop()
    female = females.popleft()

    if not male == female:
        males.append(male - 2)
        continue

    matches += 1

print_result(matches, males, females)
