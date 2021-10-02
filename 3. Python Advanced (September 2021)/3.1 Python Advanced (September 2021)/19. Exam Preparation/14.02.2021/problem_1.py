from collections import deque

fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_powers = [int(x) for x in input().split(", ")]

palm, willow, crossette = 0, 0, 0
successful = False

while fireworks_effects and explosive_powers:
    if fireworks_effects[0] <= 0 or explosive_powers[-1] <= 0:
        if fireworks_effects[0] <= 0:
            fireworks_effects.popleft()
        if explosive_powers[-1] <= 0:
            explosive_powers.pop()
        continue

    # Successful
    if all(x >= 3 for x in [palm, willow, crossette]):
        successful = True
        break

    firework = fireworks_effects.popleft()  # First firework
    explosive = explosive_powers.pop()  # Last explosive

    current_sum = firework + explosive
    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        palm += 1
        continue
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        willow += 1
        continue
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette += 1
        continue

    fireworks_effects.append(firework - 1)
    explosive_powers.append(explosive)

if all(x >= 3 for x in [palm, willow, crossette]):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
