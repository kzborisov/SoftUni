# Task 02. More Exercises - Find The Capitals

str_input = input()
result = []
for idx, letter in enumerate(str_input):
    if letter.isupper():
        result.append(idx)

print(result)
