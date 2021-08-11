# Task 10. List Manipulator

NO_MATCHES = "No matches"
INVALID_COUNT = "Invalid count"


def find_evens(list_to_check):
    return [x for x in list_to_check if x % 2 == 0]


def find_odds(list_to_check):
    return [x for x in list_to_check if not x % 2 == 0]


def rightmost_index(list_to_check, num):
    return [idx for idx, x in enumerate(list_to_check) if x == num][-1]


def exchange(idx):
    global initial_list
    if idx in range(len(initial_list)):
        left = initial_list[:idx+1]
        right = initial_list[idx+1:]
        initial_list = right + left
    else:
        print("Invalid index")


def max_even(list_to_check):
    even_nums = find_evens(list_to_check)
    try:
        max_even_num = max(even_nums)
    except ValueError:
        return
    rightmost_max = rightmost_index(list_to_check, max_even_num)
    return rightmost_max


def max_odd(list_to_check):
    odd_nums = find_odds(list_to_check)
    try:
        max_odd_num = max(odd_nums)
    except ValueError:
        return NO_MATCHES
    rightmost_max = rightmost_index(list_to_check, max_odd_num)
    return rightmost_max


def min_even(list_to_check):
    even_nums = find_evens(list_to_check)
    try:
        min_even_num = min(even_nums)
    except ValueError:
        return NO_MATCHES
    rightmost_min = rightmost_index(list_to_check, min_even_num)
    return rightmost_min


def min_odd(list_to_check):
    odd_nums = find_odds(list_to_check)
    try:
        min_odd_num = min(odd_nums)
    except ValueError:
        return NO_MATCHES
    rightmost_min = rightmost_index(list_to_check, min_odd_num)
    return rightmost_min


def first_even(list_to_check, count):
    if count > len(list_to_check):
        return INVALID_COUNT
    even_nums = find_evens(list_to_check)
    return even_nums[:count]


def first_odd(list_to_check, count):
    if count > len(list_to_check):
        return INVALID_COUNT
    odd_nums = find_odds(list_to_check)
    return odd_nums[:count]


def last_even(list_to_check, count):
    if count > len(list_to_check):
        return INVALID_COUNT
    even_nums = find_evens(list_to_check)
    return even_nums[-count:]


def last_odd(list_to_check, count):
    if count > len(list_to_check):
        return INVALID_COUNT
    odd_nums = find_odds(list_to_check)
    return odd_nums[-count:]


def max_number(list_to_check, num_type):
    if num_type == "even":
        return max_even(list_to_check)
    elif num_type == "odd":
        return max_odd(list_to_check)


def min_number(list_to_check, num_type):
    if num_type == "even":
        return min_even(list_to_check)
    elif num_type == "odd":
        return min_odd(list_to_check)


def first_numbers(list_to_check, count, num_type):
    if num_type == "even":
        return first_even(list_to_check, count)
    elif num_type == "odd":
        return first_odd(list_to_check, count)


def last_numbers(list_to_check, count, num_type):
    if num_type == "even":
        return last_even(list_to_check, count)
    elif num_type == "odd":
        return last_odd(list_to_check, count)


initial_list = list(map(int, input().split()))
cmd = input()

while not cmd == "end":
    cmd = cmd.split()
    if cmd[0] == 'exchange':
        exchange(int(cmd[1]))
    elif cmd[0] == 'max':
        print(max_number(initial_list, cmd[1]))
    elif cmd[0] == 'min':
        print(min_number(initial_list, cmd[1]))
    elif cmd[0] == 'first':
        print(first_numbers(initial_list, int(cmd[1]), cmd[2]))
    elif cmd[0] == 'last':
        print(last_numbers(initial_list, int(cmd[1]), cmd[2]))
    cmd = input()

print(initial_list)
