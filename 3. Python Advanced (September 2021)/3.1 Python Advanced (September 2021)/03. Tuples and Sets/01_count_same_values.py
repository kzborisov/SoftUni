numbers = [float(x) for x in input().split()]

numbers_count = {}

for num in numbers:
    if num not in numbers_count:
        numbers_count[num] = 0
    numbers_count[num] += 1

for key, value in numbers_count.items():
    print(f"{key} - {value} times")
