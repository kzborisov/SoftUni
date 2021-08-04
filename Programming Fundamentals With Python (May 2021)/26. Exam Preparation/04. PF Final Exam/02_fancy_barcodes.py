import re


def is_barcode_valid(barcode):
    pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
    match = re.search(pattern, barcode)
    if match:
        return True
    print(f"Invalid barcode")
    return False


def get_product_group(barcode):
    if is_barcode_valid(barcode):
        product_group = ''.join([x for x in barcode if x.isdigit()])
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")


n = int(input())
for _ in range(n):
    current_barcode = input()
    get_product_group(current_barcode)
