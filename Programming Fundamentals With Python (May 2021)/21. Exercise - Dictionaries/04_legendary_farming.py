def add_to_junk(key_materials_dict, material_to_add, qty_to_add):
    if material_to_add not in key_materials_dict:
        key_materials_dict[material_to_add] = qty_to_add
    else:
        key_materials_dict[material_to_add] += qty_to_add


def is_item_obtained():
    global item_obtained
    if key_materials['shards'] >= 250:
        item_obtained = "Shadowmourne"
        key_materials['shards'] -= 250
        return True
    elif key_materials['fragments'] >= 250:
        item_obtained = "Valanyr"
        key_materials['fragments'] -= 250
        return True
    elif key_materials['motes'] >= 250:
        item_obtained = "Dragonwrath"
        key_materials['motes'] -= 250
        return True
    return False


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while not item_obtained:
    materials = input().split()
    for i in range(0, len(materials), 2):
        qty = int(materials[i])
        material = materials[i+1].lower()
        if material in key_materials:
            key_materials[material] += qty
        else:
            add_to_junk(junk, material, qty)

        if is_item_obtained():
            break

print(f"{item_obtained} obtained!")
for k, v in sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k}: {v}")

for k, v in sorted(junk.items(), key=lambda kvp: kvp[0]):
    print(f"{k}: {v}")
