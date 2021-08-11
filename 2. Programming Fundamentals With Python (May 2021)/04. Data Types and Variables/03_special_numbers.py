# Task 03. Special Numbers
num = int(input())

digits = [x for x in range(1,num+1)]
is_special = False

for digit in digits:
    digit_iter = [int(x) for x in str(digit)]
    if sum(digit_iter) == 5 or sum(digit_iter) == 7 or sum(digit_iter) == 11:
        is_special = True
    else:
        is_special = False

    print(f'{digit} -> {is_special}')
