# Task 05. More Exercises Multiplication Sign

def is_negative(num):
    if num == 0:
        return 0
    elif num < 0:
        return -1
    return 1


num1 = float(input())
num2 = float(input())
num3 = float(input())

list_of_nums = [num1, num2, num3]
is_zero = False
number_of_negative = 0


for num in list_of_nums:
    if is_negative(num) == 0:
        is_zero = True
    elif is_negative(num) == -1:
        number_of_negative += 1


if is_zero:
    print('zero')
elif number_of_negative % 2 == 0:
    print('positive')
else:
    print('negative')
