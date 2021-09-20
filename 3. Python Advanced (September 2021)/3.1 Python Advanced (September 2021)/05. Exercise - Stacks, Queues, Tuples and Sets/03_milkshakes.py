from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while True:
    if not chocolates or not cups_of_milk or milkshakes == 5:
        break

    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 or milk <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)
        if milk > 0:
            cups_of_milk.appendleft(milk)
    elif chocolate == milk:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates])}')
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f'Milk: {", ".join([str(el) for el in cups_of_milk])}')
else:
    print('Milk: empty')
