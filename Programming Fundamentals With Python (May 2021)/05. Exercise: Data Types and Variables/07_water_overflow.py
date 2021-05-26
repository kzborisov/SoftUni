# Task 07. Water Overflow
lines = int(input())
CAPACITY = 255
litters_filled = 0

for i in range(lines):
    water = int(input())
    if CAPACITY - water < 0:
        print('Insufficient capacity!')
    else:
        CAPACITY -= water
        litters_filled += water

print(litters_filled)
