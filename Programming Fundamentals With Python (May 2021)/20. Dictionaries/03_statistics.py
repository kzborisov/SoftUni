# Task 03. Statistics
def add_to_dict(product: str, quantity: int):
    if product not in stock:
        stock[product] = quantity
    else:
        stock[product] += quantity


cmd = input()
stock = {}

while not cmd == "statistics":
    key = cmd.split(': ')[0]
    value = cmd.split(': ')[1]
    add_to_dict(key, int(value))
    cmd = input()


print("Products in stock:")
for product in stock:
    print(f"- {product}: {stock[product]}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
