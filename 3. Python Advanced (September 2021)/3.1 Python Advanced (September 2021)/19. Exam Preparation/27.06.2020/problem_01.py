from collections import deque

bombs = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]

materials = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0],
}
bombs_ready = False

while bombs and casings:
    if all(v[1] >= 3 for v in materials.values()):
        bombs_ready = True
        break
    bomb = bombs.popleft()
    case = casings.pop()
    curr_sum = bomb + case
    for material in materials:
        if materials[material][0] == curr_sum:
            materials[material][1] += 1
            break
    else:
        case -= 5
        bombs.appendleft(bomb)
        casings.append(case)

res = ""
if bombs_ready:
    res += 'Bene! You have successfully filled the bomb pouch!\n'
else:
    res += "You don't have enough materials to fill the bomb pouch.\n"
if bombs:
    res += f'Bomb Effects: {", ".join(map(str, bombs))}\n'
else:
    res += 'Bomb Effects: empty\n'
if casings:
    res += f'Bomb Casings: {", ".join(map(str, casings))}\n'
else:
    res += 'Bomb Casings: empty\n'
for bomb, count in sorted(materials.items()):
    res += f'{bomb}: {count[1]}\n'

print(res)