rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(",")] for _ in range(rows)]
print(sum([x for y in matrix for x in y]))
print(matrix)
