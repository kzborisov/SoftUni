# Task 01 - More Exercises - Find The Largest
num = input()
digits = sorted([int(x) for x in num], reverse=True)
result = ''.join([str(x) for x in digits])
print(result)
