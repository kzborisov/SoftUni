rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
column_sums = [sum([row[i] for row in matrix]) for i in range(0, len(matrix[0]))]
print(*column_sums, sep="\n")
