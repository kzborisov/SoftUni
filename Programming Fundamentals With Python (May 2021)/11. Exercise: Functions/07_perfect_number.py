# Task 07. Perfect Number

def sum_of_divisors(num):
    return sum([x for x in range(1, num) if num % x == 0])


def perfect_number(num):
    if num == sum_of_divisors(num):
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
