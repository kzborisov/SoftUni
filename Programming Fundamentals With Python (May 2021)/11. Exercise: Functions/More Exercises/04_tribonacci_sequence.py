# Task 04. More Exercises - Tribonacci Sequence


def tribonacci(n):
    tribonacci_seq = [1, 1, 2]
    if n < 3:
        return [str(x) for x in tribonacci_seq[:n]]
    while len(tribonacci_seq) < n:
        next_num = sum(tribonacci_seq[-3:])
        tribonacci_seq.append(next_num)
    return [str(x) for x in tribonacci_seq]


length = int(input())
print(' '.join(tribonacci(length)))
