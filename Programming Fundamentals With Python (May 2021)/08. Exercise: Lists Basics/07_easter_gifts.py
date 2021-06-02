# Task 07. Easter Gifts

def find_and_replace(input_list, old_string, new_string):
    while old_string in input_list:
        ind = input_list.index(old_string)
        input_list[ind] = new_string
    return input_list


gifts = input().split()

while True:
    cmd = input()
    if cmd == "No Money":
        break
    command = cmd.split()
    if command[0] == "OutOfStock":
        gift = command[1]
        gifts = find_and_replace(gifts, gift, None)
    elif command[0] == 'Required':
        gift = command[1]
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = gift
    elif command[0] == 'JustInCase':
        gift = command[1]
        gifts[-1] = gift

result = [x for x in gifts if x is not None]
print(' '.join(result))
