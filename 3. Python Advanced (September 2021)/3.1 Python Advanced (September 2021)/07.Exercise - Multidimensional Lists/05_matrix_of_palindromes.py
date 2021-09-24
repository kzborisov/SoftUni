n, m = map(int, input().split())
matrix = []

for row in range(n):
    for col in range(m):
        first_and_last = chr(ord("a") + row)
        middle = chr(ord("a") + row + col)
        print(f"{first_and_last}{middle}{first_and_last}", end=" ")
    print()
