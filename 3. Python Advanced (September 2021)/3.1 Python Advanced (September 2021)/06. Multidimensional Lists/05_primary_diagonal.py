size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
print(sum([matrix[x][x] for x in range(size)]))
