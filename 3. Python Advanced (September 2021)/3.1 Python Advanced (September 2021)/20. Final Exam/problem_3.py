def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    items = 0
    result = ""
    for product, product_info in kwargs.items():
        price, quantity = product_info
        current_price = price * quantity

        if current_price > budget:
            continue
        budget -= current_price
        items += 1
        result += f"You bought {product} for {current_price:.2f} leva.\n"
        if items == 5:
            return result

    return result


# print(shopping_list(100,
#                     microwave=(150, 1),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(150,
#                     jeans=(120, 2),
#                     ))
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     microwave=(150, 1),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
