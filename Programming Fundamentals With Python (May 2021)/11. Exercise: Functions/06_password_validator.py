# Task 06. Password Validator

def validate_len(password):
    if not len(password) in range(6, 11):
        print('Password must be between 6 and 10 characters')
        return False
    return True


def validate_chars(password):
    chars_verified = True
    for char in password:
        if not char.isalpha() and not char.isdigit():
            chars_verified = False
    if not chars_verified:
        print('Password must consist only of letters and digits')
        return False
    return True


def validate_contains_two_digits(password):
    numbers_in_password = [x for x in password if x.isdigit()]
    if len(numbers_in_password) < 2:
        print('Password must have at least 2 digits')
        return False
    return True


def validate_password(password):
    is_valid_len = validate_len(password)
    is_valid_chars = validate_chars(password)
    contains_two_digits = validate_contains_two_digits(password)

    if is_valid_len and is_valid_chars and contains_two_digits:
        print('Password is valid')


password = input()
validate_password(password)
