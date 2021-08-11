
targets = [int(x) for x in input().split()]
cmd = input()

while not cmd == "End":
    idx = int(cmd)

    if 0 <= idx <= len(targets) - 1:
        current_value = targets[idx]
        targets[idx] = -1

        for i in range(len(targets)):
            if i == idx:
                continue
            if targets[i] == - 1:
                continue

            if targets[i] > current_value:
                targets[i] -= current_value
            elif targets[i] <= current_value:
                targets[i] += current_value

    cmd = input()

shot_targets = len([x for x in targets if x == -1])
print(f"Shot targets: {shot_targets} -> {' '.join([ str(x) for x in targets])}")
