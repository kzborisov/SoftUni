from math import log


def calculate_log(x, base_str):
    if base_str == "natural":
        return log(x)

    base = int(base_str)
    return log(x, base)


number = int(input())
base = input()
print(f"{calculate_log(number, base):.2f}")
print(f"{calculate_log(10, 10):.2f}")
print(f"{calculate_log(1024, 2):.2f}")
print(f"{calculate_log(10, 'natural'):.2f}")
