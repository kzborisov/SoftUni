from collections import deque

cups = deque([int(x) for x in input().split()])
filled_bottles = [int(x) for x in input().split()]
litters_wasted = 0

while True:
    if not cups or not filled_bottles:
        break

    curr_cup = cups[0]
    curr_bottle = filled_bottles.pop()
    water_to_remove = curr_bottle
    curr_bottle -= curr_cup
    cups[0] -= water_to_remove

    if cups[0] <= 0:
        cups.popleft()
    if curr_bottle >= 0:
        litters_wasted += curr_bottle

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in filled_bottles])}")
elif not filled_bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {litters_wasted}")
