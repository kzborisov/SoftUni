# Task 04. Orders

def orders(product, quantity):
    prices = {
        'coffee': 1.5,
        'water': 1,
        'coke': 1.40,
        'snacks': 2
    }
    return prices[product] * quantity


prod = input()
quantity = int(input())

print(f"{orders(prod, quantity):.2f}")
