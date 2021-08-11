# Task 02. Add and Subtract

def add_and_subtract(a, b, c):
    def sum_numbers(a, b):
        return sum([a, b])

    sum_nums = sum_numbers(a, b)

    def subtract(numbers_sum, third_num):
        return numbers_sum - third_num

    return subtract(sum_nums, c)


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))
