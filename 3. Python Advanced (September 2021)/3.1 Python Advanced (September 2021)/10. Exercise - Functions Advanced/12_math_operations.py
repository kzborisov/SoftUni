from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    index = 0
    while args:
        index %= 4
        current_arg = args.popleft()

        if index == 0:
            kwargs["a"] += current_arg
        elif index == 1:
            kwargs["s"] -= current_arg
        elif index == 2:
            if not current_arg == 0:
                kwargs["d"] /= current_arg
        elif index == 3:
            kwargs["m"] *= current_arg
        index += 1
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
