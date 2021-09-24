rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary = [matrix[x][x] for x in range(rows)]
secondary = [matrix[x][rows - x - 1] for x in range(rows)]

difference = abs(sum(primary) - sum(secondary))
print(difference)
