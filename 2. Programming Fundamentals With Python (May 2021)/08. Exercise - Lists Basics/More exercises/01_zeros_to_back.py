# Task 01. More Exercises Zeros to Back
all_integers = input().split(', ')
zeros = [int(x) for x in all_integers if x == '0']
integers = [int(x) for x in all_integers if not x == '0']
print(integers+zeros)
