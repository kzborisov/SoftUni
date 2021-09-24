def calculate_sum(submatrix):
    return sum(map(sum, submatrix))


rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = 0
best_matrix = []
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        matrix_sum = matrix[row][col] + \
                     matrix[row][col + 1] + \
                     matrix[row][col + 2] + \
                     matrix[row + 1][col] + \
                     matrix[row + 1][col + 1] + \
                     matrix[row + 1][col + 2] + \
                     matrix[row + 2][col] + \
                     matrix[row + 2][col + 1] + \
                     matrix[row + 2][col + 2]
        # matrix_sum = calculate_sum(sub_matrix)
        if matrix_sum > max_sum:
            max_sum, best_row, best_col = matrix_sum, row, col
            # best_matrix = sub_matrix

print(f"Sum = {max_sum}")
for r in range(best_row, best_row + 3):
    for c in range(best_col, best_col + 3):
        print(matrix[r][c], end=" ")
    print()
