def find_missing(numbers):
    for number in range(min(numbers), max(numbers)):
        if number not in numbers:
            return number


def numbers_searching(*args):
    unique_numbers = set()
    duplicates = set()
    for number in args:
        if number in unique_numbers:
            duplicates.add(number)
        unique_numbers.add(number)
    missing_number = find_missing(args)

    return [missing_number, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
