# Task 04. Sum of Chars
lines = int(input())

chars = []

for line in range(lines):
    char = input()
    chars.append(ord(char))

print(f'The sum equals: {sum(chars)}')
