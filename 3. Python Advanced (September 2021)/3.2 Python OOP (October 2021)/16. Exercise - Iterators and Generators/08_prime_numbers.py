def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def get_primes(integers):
    for integer in integers:
        if is_prime(integer):
            yield integer


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
