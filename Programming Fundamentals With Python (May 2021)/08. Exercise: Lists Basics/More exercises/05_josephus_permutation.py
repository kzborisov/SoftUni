# Task 05. More Exercises Josephus Permutation
initial_sequence = input().split()
kill = int(input())

index = 0
counter = 0
result = []

while len(initial_sequence) > 0:
    counter += 1
    if counter % kill == 0:
        result.append(initial_sequence.pop(index))
    else:
        index += 1

    if index >= len(initial_sequence):
        index = 0

print(f"[{','.join(result)}]")
