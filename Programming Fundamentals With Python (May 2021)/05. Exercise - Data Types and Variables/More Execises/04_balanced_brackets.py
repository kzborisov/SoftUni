# Task 04. More Exercises - Balanced Brackets


def matching_brackets(arr_input):
    not_balanced_count = 0
    pairs = [i+j for i, j in zip(arr_input[::2], arr_input[1::2])]
    for pair in pairs:
        if not pair == '()':
            not_balanced_count += 1

    if not_balanced_count == 0:
        return True
    return False


lines = int(input())
equation = []

for _ in range(lines):
    char = input()
    if char == '(' or char == ')':
        equation.append(char)

if matching_brackets(equation):
    print('BALANCED')
else:
    print('UNBALANCED')
