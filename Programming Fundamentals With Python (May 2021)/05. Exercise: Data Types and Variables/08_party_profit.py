# Task 08. Party Profit
size = int(input())
days = int(input())
coins = 0

for day in range(1, days+1):
    coins_for_food = 2
    if day % 10 == 0:
        size -= 2
    if day % 15 == 0:
        size += 5

    if day % 3 == 0:
        coins_for_food += 3
    if day % 5 == 0:
        coins += 20 * size
        if day % 3 == 0:
            coins_for_food += 2
    coins += 50 - coins_for_food * size

print(f'{size} companions received {coins//size} coins each.')
