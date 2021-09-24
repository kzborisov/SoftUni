rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

squares_found = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == \
                matrix[row][col + 1] == \
                matrix[row + 1][col] == \
                matrix[row + 1][col + 1]:
            squares_found += 1

print(squares_found)
