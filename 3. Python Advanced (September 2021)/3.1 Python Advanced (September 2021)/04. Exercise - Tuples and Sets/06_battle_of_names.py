n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    name_ascii_sum = sum(ord(x) for x in name)
    result = name_ascii_sum // row

    odd_set.add(result) if not result % 2 == 0 else even_set.add(result)

odd_set_sum = sum(x for x in odd_set)
even_set_sum = sum(x for x in even_set)

if odd_set_sum == even_set_sum:
    result = odd_set.union(even_set)
elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

result = ", ".join(str(x) for x in result)
print(result)
