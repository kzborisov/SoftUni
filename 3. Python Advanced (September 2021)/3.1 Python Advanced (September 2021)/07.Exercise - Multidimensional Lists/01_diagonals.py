row = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]

primary_diagonal = [matrix[x][x] for x in range(row)]
secondary_diagonal = [matrix[x][row - x - 1] for x in range(row)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}."
      f" Sum: {sum(primary_diagonal)}")

print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}."
      f" Sum: {sum(secondary_diagonal)}")
