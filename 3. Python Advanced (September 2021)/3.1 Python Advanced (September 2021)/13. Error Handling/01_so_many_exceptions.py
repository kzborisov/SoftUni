# numbers_list = [int(x) for x in input().split(", ")]


def find_sum(numbers_list):
    result = 1
    for i in range(len(numbers_list)):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif number <= 10:
            result /= number

    return result


print(find_sum([1, 4, 5]), 20)
print(find_sum([4, 5, 6, 1, 3]), 20)
print(find_sum([2, 5, 10]), 20)
