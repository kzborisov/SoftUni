from collections import deque

materials = [int(x) for x in input().split()]
genie_magic = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": [range(100, 200), 0],
    "Porcelain Sculpture": [range(200, 300), 0],
    "Gold": [range(300, 400), 0],
    "Diamond Jewellery": [range(400, 500), 0],
}


def check_in_table(the_sum):
    for present, present_info in presents.items():
        if the_sum in present_info[0]:
            presents[present][1] += 1
            return presents


def print_result(is_successful):
    if is_successful:
        print("The wedding presents are made!")
    else:
        print("Aladdin does not have enough wedding presents.")

    if materials:
        print(f"Materials left: {', '.join(str(x) for x in materials)}")
    if genie_magic:
        print(f"Magic left: {', '.join(str(x) for x in genie_magic)}")

    for gift, gift_info in sorted(presents.items()):
        if gift_info[1] >= 1:
            print(f"{gift}: {gift_info[1]}")


success = False
while materials and genie_magic:

    material = materials.pop()
    magic = genie_magic.popleft()

    current_sum = material + magic

    if check_in_table(current_sum):
        continue

    if current_sum < 100:
        if current_sum % 2 == 0:
            materials.append(material * 2)
            genie_magic.appendleft(magic * 3)
            material = materials.pop()
            magic = genie_magic.popleft()
            current_sum = material + magic
            check_in_table(current_sum)
        else:
            current_sum *= 2
            check_in_table(current_sum)
    elif current_sum > 499:
        current_sum //= 2
        check_in_table(current_sum)

if (presents["Gemstone"][1] >= 1 and presents["Porcelain Sculpture"][1] >= 1) or \
        presents["Gold"][1] >= 1 and presents["Diamond Jewellery"][1] >= 1:
    success = True

print_result(success)
