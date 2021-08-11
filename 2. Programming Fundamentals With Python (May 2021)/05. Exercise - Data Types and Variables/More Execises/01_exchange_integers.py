# Task 01. More exercises Exchange Integers
a = int(input())
b = int(input())

result = 'Before:\n'
result += f'a = {a}\n'
result += f'b = {b}\n'

a, b = b, a

result += 'After:\n'
result += f'a = {a}\n'
result += f'b = {b}\n'

print(result)
