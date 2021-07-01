# Task 09. Hello, France

def validate_price(items_and_prices):
    item = items_and_prices.split('->')[0]
    prices = float(items_and_prices.split('->')[1])
    if item == 'Clothes' and prices <= 50 or \
            item == 'Shoes' and prices <= 35.00 or \
            item == 'Accessories' and prices <= 20.50:
        return True
    return False


items_and_prices = input().split('|')
budget = float(input())
initial_budget = budget

new_prices = []
for item in items_and_prices:
    item_price = float(item.split('->')[1])

    if budget - item_price < 0:
        continue

    if validate_price(item):
        budget -= item_price
        new_price = item_price + (item_price * 0.40)
        new_prices.append(new_price)

earned = sum(new_prices)
profit = budget + (earned-initial_budget)
budget += earned
if budget >= 150:
    result = 'Hello, France!'
else:
    result = 'Time to go.'

print(' '.join([f'{x:.2f}' for x in new_prices]))
print(f'Profit: {profit:.2f}')
print(result)
