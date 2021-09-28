def print_even_or_odd(cmd, numbers_list):
    if cmd == "Odd":
        return sum([x for x in numbers_list if not x % 2 == 0]) * len(numbers)
    return sum([x for x in numbers_list if x % 2 == 0]) * len(numbers)


command = input()
numbers = [int(x) for x in input().split()]
print(print_even_or_odd(command, numbers))
