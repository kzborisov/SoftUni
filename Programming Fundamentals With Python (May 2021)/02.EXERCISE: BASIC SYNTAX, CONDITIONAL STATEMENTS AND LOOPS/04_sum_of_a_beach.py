# Task 04. More Exercises - Sum of a Beach
str_input = input().lower()
words = ['sand', 'water', 'fish', 'sun']

count = 0

for word in words:
    if word in str_input:
        count += str_input.count(word)

print(count)
