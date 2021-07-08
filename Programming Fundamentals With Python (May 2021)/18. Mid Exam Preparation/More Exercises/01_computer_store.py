prices_without_tax = input()
total_price = 0
total_without_tax = 0
taxes = 0

while True:
    if prices_without_tax == "special" or \
            prices_without_tax == "regular":
        break
    price = float(prices_without_tax)
    tax = price * 0.2

    prices_without_tax = input()
    if price < 0:
        print("Invalid price!")
        continue
    taxes += tax
    total_without_tax += price
    total_price += price + tax

if total_price <= 0:
    print("Invalid order!")
    exit()

if prices_without_tax == "special":
    total_price *= 0.90


print(f"Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {total_without_tax:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n"
      "-----------\n"
      f"Total price: {total_price:.2f}$")
