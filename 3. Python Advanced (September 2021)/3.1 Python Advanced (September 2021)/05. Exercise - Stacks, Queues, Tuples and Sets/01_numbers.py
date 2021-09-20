first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()
    cmd = command[0]
    sequence = command[1]

    if cmd == "Add":
        numbers = [int(x) for x in command[2:]]
        if sequence == "First":
            first.update(numbers)
        elif sequence == "Second":
            second.update(numbers)
    elif cmd == "Remove":
        numbers = [int(x) for x in command[2:]]
        if sequence == "First":
            first.difference_update(numbers)
        elif sequence == "Second":
            second.difference_update(numbers)
    elif cmd == "Check":
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
