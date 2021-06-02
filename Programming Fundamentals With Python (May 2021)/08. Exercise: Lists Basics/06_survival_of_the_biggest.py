# Task 06. Survival of the Biggest
numbers = list(map(int, input().split()))
count = int(input())

sorted_nums = [x for x in sorted(numbers, reverse=True)[:len(numbers)-count]]

result = [str(x) for x in numbers if x in sorted_nums]
print(', '.join(result))
