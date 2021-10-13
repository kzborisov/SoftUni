from collections import deque


def print_result(is_successful, bombs, casings, prices):
    if is_successful:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    if bombs:
        print(f"Bomb Effects: {', '.join(str(x) for x in bombs)}")
    else:
        print("Bomb Effects: empty")

    if casings:
        print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
    else:
        print("Bomb Casings: empty")

    for bomb, values in sorted(prices.items()):
        print(f"{bomb}: {values[1]}")


bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

prices = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0],
}
success = False

while bomb_effects and bomb_casings:
    if all(v[1] >= 3 for k, v in prices.items()):
        success = True
        break
    current_bomb = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    the_sum = current_bomb + current_casing
    for bomb, values in prices.items():
        if the_sum == values[0]:
            prices[bomb][1] += 1
            break

    else:
        bomb_casings.append(current_casing - 5)
        bomb_effects.appendleft(current_bomb)

print_result(success, bomb_effects, bomb_casings, prices)
