food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
weight = float(input()) * 1000

AMOUNT_PER_DAY = 300

for day in range(1, 30 + 1):
    food_quantity -= AMOUNT_PER_DAY

    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= (weight / 3)

    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        print("Merry must go to the pet store!")
        exit()

print(f"Everything is fine! Puppy is happy! Food: {food_quantity/1000:.2f},"
      f" Hay: {hay_quantity/1000:.2f}, Cover: {cover_quantity/1000:.2f}.")
