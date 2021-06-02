# Task 02. Multiples List
factor = int(input())
count = int(input())

result = []
current_num = 1
while len(result) < count:
    if current_num % factor == 0:
        result.append(current_num)
    current_num += 1

print(result)
