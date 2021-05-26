# Task 02. More Exercises Prime Numbers Check
num = int(input())


def check_prime(n):
    """
    :param n
    :return True if integer is prime, otherwise False
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


print(check_prime(num))
