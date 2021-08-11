# Task 05. Palindrome Integers

def check_palindrome(list_of_numbers):
    for num in list_of_numbers:
        if num == num[::-1]:
            yield True
        else:
            yield False


list_of_nums = input().split(", ")
my_generator = check_palindrome(list_of_nums)
for i in my_generator:
    print(i)
