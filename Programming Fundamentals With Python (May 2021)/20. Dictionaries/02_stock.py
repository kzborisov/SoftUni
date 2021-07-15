# Task 02. Stock
def product_in_bakey(product, bakery_dict):
    if product in bakery_dict:
        return f'We have {bakery_dict[product]} of {product} left'
    return f'Sorry, we don\'t have {product}'


def add_to_dict(input_lst):
    output_dict = {}
    for i in range(0, len(input_lst), 2):
        key = input_lst[i]
        value = input_lst[i + 1]
        output_dict[key] = int(value)
    return output_dict


inventory = input().split()
searched_products = input().split()
bakery = add_to_dict(inventory)
print(bakery)

for product in searched_products:
    print(product_in_bakey(product, bakery))
