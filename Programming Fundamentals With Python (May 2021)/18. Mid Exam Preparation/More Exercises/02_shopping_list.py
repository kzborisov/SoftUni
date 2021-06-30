"""
t’s the end of the week and it is time for you to go shopping,
so you need to create a shopping list first.

Input
You will receive an initial list with groceries separated by "!".
After that you will be receiving 4 types of commands, until you receive "Go Shopping!"
    • Urgent {item}
        add the item at the start of the list.
        If the item already exists, skip this command.
    • Unnecessary {item}
        remove the item with the given name,
        only if it exists in the list. Otherwise skip this command.
    • Correct {oldItem} {newItem}
        if the item with the given old name exists,
        change its name with the new one.
        If it doesn't exist, skip this command.
    • Rearrange {item}
        if the grocery exists in the list,
        remove it from its current position and add it at the end of the list.

Constraints
    • There won`t be any duplicate items in the initial list

Output
Print the list with all the groceries, joined by ", ".
    • "{firstGrocery}, {secondGrocery}, …{nthGrocery}"

Test Input:
Tomatoes!Potatoes!Bread
Unnecessary Milk
Urgent Tomatoes
Go Shopping!

Test Output
Tomatoes, Potatoes, Bread

Test Input:
Milk!Pepper!Salt!Water!Banana
Urgent Salt
Unnecessary Grapes
Correct Pepper Onion
Rearrange Grapes
Correct Tomatoes Potatoes
Go Shopping!

Test Output:
Milk, Onion, Salt, Water, Banana
"""


def urgent(shopping_lst, item_to_add):
    if item_to_add not in shopping_lst:
        shopping_lst.insert(0, item_to_add)


def unnecessary(shopping_lst, item_to_temove):
    if item_to_temove in shopping_lst:
        shopping_lst.remove(item_to_temove)


def correct(shopping_lst, old, new):
    if old in shopping_lst:
        shopping_lst[shopping_list.index(old)] = new


def rearrange(shopping_lst, item_to_rearrange):
    if item_to_rearrange in shopping_lst:
        shopping_lst.append(
            shopping_lst.pop(
                shopping_lst.index(item_to_rearrange))
        )


shopping_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    cmd = command.split()[0]

    if cmd == "Urgent":
        item = command.split()[1]
        urgent(shopping_list, item)
    elif cmd == "Unnecessary":
        item = command.split()[1]
        unnecessary(shopping_list, item)
    elif cmd == "Correct":
        old_item = command.split()[1]
        new_item = command.split()[2]
        correct(shopping_list, old_item, new_item)
    elif cmd == "Rearrange":
        item = command.split()[1]
        rearrange(shopping_list, item)

    command = input()
print(*shopping_list, sep=", ")
