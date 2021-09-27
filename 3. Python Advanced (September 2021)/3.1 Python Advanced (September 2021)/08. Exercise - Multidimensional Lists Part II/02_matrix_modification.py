def is_valid_index(r, c, size):
    return r in range(size) and c in range(size)


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    command = line.split()[0]
    row, col, value = map(int, line.split()[1:])

    if not is_valid_index(row, col, rows):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")
