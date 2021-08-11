# Task 09. Factorial Division

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1


first_num = int(input())
second_num = int(input())

result = factorial(first_num) / factorial(second_num)
print(f"{result:.2f}")
