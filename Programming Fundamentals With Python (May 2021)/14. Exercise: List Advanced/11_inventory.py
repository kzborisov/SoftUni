# Task 11. Inventory
def collect(lst, item):
    if not item in lst:
        lst.append(item)


def drop(lst, item):
    if item in lst:
        lst.remove(item)


def combine(lst, old_item, new_item):
    if old_item in lst:
        idx = lst.index(old_item) + 1
        lst.insert(idx, new_item)


def renew(lst, item):
    if item in lst:
        lst.append(lst.pop(lst.index(item)))


collecting_items = input().split(", ")
command = input()

while not command == "Craft!":
    cmd = command.split(" - ")[0]
    item = command.split(" - ")[1]

    if cmd == "Collect":
        collect(collecting_items, item)
    elif cmd == "Drop":
        drop(collecting_items, item)
    elif cmd == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        combine(collecting_items, old_item, new_item)
    elif cmd == "Renew":
        renew(collecting_items, item)

    command = input()

print(", ".join(collecting_items))
