from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
task_done = False

presents_table = {
    "Doll": {'price': 150, 'crafted': False, 'count': 0},
    "Wooden train": {'price': 250, 'crafted': False, 'count': 0},
    "Teddy bear": {'price': 300, 'crafted': False, 'count': 0},
    "Bicycle": {'price': 400, 'crafted': False, 'count': 0},
}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    present_magic = material * magic

    is_found = False

    for present, present_info in presents_table.items():
        if present_magic == present_info['price']:
            is_found = True
            present_info['crafted'] = True
            present_info['count'] += 1

    if present_magic < 0:
        magic_sum = material + magic
        materials.append(magic_sum)

    if not is_found and present_magic > 0:
        materials.append(material + 15)

    if material == 0 and magic == 0:
        continue
    elif material == 0:
        magic_levels.appendleft(magic)
    elif magic == 0:
        materials.append(material)

if presents_table['Doll']['crafted'] and presents_table['Wooden train']['crafted'] \
        or presents_table['Teddy bear']['crafted'] and presents_table['Bicycle']['crafted']:
    task_done = True

if task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials]))}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for present, present_info in sorted(presents_table.items()):
    if present_info['crafted']:
        print(f"{present}: {present_info['count']}")
