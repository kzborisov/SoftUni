# Task 09. Easter Cozonacs

budget = float(input())
flour = float(input())

recipe = {
    'eggs': 1,
    'flour': 1,
    'milk': 0.250
}
prices = {
    'eggs': flour * 0.75,
    'milk': (flour * 1.25) / 4,
}

cozonacs = 0
eggs_received = 0
price = prices['eggs'] + prices['milk'] + flour

while budget > price:
    budget -= price
    cozonacs += 1
    eggs_received += 3
    if cozonacs % 3 == 0:
        eggs_received -= cozonacs - 2
print(f'You made {cozonacs} cozonacs! Now you have {eggs_received} eggs and {budget:.2f}BGN left.')
