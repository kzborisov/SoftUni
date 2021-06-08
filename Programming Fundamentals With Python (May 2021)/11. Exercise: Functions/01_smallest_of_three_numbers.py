# Task 01. Smallest of Three Numbers

first = int(input())
second = int(input())
third = int(input())

numbers_list = [first, second, third]
print((lambda numbers: min(numbers_list))(numbers_list))
