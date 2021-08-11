# Task 05. Even Numbers

numbers = list(map(lambda x: int(x), input().split(", ")))

print([x for x in range(len(numbers)) if numbers[x] % 2 == 0])
