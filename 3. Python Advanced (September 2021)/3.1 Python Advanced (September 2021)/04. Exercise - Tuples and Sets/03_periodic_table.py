n = int(input())
periodic_table = set()

for _ in range(n):
    elements = input().split()
    periodic_table.update(elements)

[print(x) for x in periodic_table]
