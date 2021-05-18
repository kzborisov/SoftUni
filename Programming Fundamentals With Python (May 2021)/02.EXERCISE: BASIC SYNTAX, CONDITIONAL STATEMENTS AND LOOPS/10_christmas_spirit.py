# Task 10. Christmas Spirit

quantity = int(input())
days = int(input())

prices_map = {
    'Ornament Set': 2,
    'skirt': 5,
    'garlands': 3,
    'lights': 15
}

christmas_spirit = 0
budget = 0

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        budget += prices_map['Ornament Set'] * quantity
    if day % 3 == 0:
        christmas_spirit += 13
        budget += prices_map['skirt']\
                  * quantity\
                  + prices_map['garlands']\
                  * quantity
    if day % 5 == 0:
        christmas_spirit += 17
        budget += prices_map['lights'] * quantity
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += prices_map['skirt']\
                  + prices_map['garlands']\
                  + prices_map['lights']

if days % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')