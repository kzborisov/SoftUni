rows = int(input())
matrix = [int(x) for y in [input().split(", ") for _ in range(rows)] for x in y]

print(matrix)
