# Product: [price, qty]
products = {}
command = input()

while not command == "buy":
    product, price, qty = command.split()
    if product not in products:
        products[product] = [float(price), int(qty)]
    else:
        products[product][1] += int(qty)
        if not products[product][0] == float(price):
            products[product][0] = float(price)
    command = input()

{print(f"{k} -> {(v[0] * v[1]):.2f}") for k, v in products.items()}