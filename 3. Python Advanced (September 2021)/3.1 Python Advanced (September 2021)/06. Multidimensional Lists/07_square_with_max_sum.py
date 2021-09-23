# Read matrix

# r = 0 ... n - 1
# c = 0 ... n - 1

n, m = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

sums = []

for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1]
        sums.append((current_sum, r, c))

max_sum = max(sums)
max_row = max_sum[1]
max_col = max_sum[2]
square = [
    [matrix[max_row][max_col], matrix[max_row][max_col + 1]],
    [matrix[max_row + 1][max_col], matrix[max_row + 1][max_col + 1]]
]
for r in square:
    for c in r:
        print(c, end=" ")
    print()
print(max_sum[0])
