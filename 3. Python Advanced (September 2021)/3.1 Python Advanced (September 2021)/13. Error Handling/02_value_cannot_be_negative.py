class ValueCannotBeNegativeError(Exception):
    pass


numbers = [int(input()) for _ in range(5)]
# try:
for number in numbers:
    if number < 0:
        raise ValueCannotBeNegativeError
