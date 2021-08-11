"""
You will receive a journal with some Collecting items, separated with ', ' (comma and space).
After that, until receiving "Craft!" you will be receiving different commands.

Commands (split by " - "):
    • "Collect - {item}"
        Receiving this command,you should add the given item in your inventory.
        If the item already exists, you should skip this line.
    • "Drop - {item}"
        You should remove the item from your inventory, if it exists.
    • "Combine Items - {oldItem}:{newItem}"
        You should check if the old item exists,
        if so, add the new item after the old one.
        Otherwise, ignore the command.
    • "Renew – {item}"
        If the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).

Test Input:
Iron, Wood, Sword
Collect - Gold
Drop - Wood
Craft!
Test Output:
Iron, Sword, Gold


Iron, Sword
Drop - Bronze
Combine Items - Sword:Bow
Renew - Iron
Craft!
Test Output:
Sword, Bow, Iron
"""


def collect(items, found_item):
    if found_item not in items:
        items.append(found_item)


def drop(items, item_to_remove):
    if item_to_remove in items:
        items.remove(item_to_remove)


def combine_items(items, old, new):
    if old in items:
        idx = items.index(old)
        items.insert(idx+1, new)


def renew(items, item_to_renew):
    if item_to_renew in items:
        items.append(
            items.pop(
                items.index(item_to_renew)))


inventory = input().split(", ")
cmd = input()


while not cmd == "Craft!":
    cmd = cmd.split(" - ")
    command = cmd[0]
    item = cmd[1]

    if command == "Collect":
        collect(inventory, item)
    elif command == "Drop":
        drop(inventory, item)
    elif command == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        combine_items(inventory, old_item, new_item)
    elif command == "Renew":
        renew(inventory, item)

    cmd = input()

print(*inventory, sep=", ")
