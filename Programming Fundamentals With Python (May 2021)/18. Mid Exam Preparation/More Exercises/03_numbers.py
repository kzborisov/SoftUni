def average(lst):
    return sum(lst) // len(lst)


numbers = [int(x) for x in input().split()]
result = sorted([x for x in numbers if x > average(numbers)], reverse=True)

if not result:
    print('No')
else:
    print(*result[:5], sep=" ")
