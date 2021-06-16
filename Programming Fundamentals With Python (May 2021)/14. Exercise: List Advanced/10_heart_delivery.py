# Task 10. Heart Delivery
def was_successfull(lst):
    if all(x == 0 for x in lst):
        return "Mission was successful."
    else:
        return f"Cupid has failed {len([x for x in lst if not x == 0])} places."


def get_position(pos, lst):
    if pos > len(lst) - 1:
         return 0
    return pos


def had_valentines_day(pos, lst, passed_collection):
    if lst[pos] <= 0:
        passed_collection.append(pos)
        print(f"Place {pos} has Valentine's day.")


neighborhood = list(map(int, input().split("@")))

jump_cmd = input()
current_position = 0
had_valentines_index = []

while not jump_cmd == "Love!":
    distance = int(jump_cmd.split()[1])
    current_position += distance
    current_position = get_position(current_position, neighborhood)

    if current_position in had_valentines_index:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neighborhood[current_position] -= 2
        had_valentines_day(current_position, neighborhood, had_valentines_index)
    jump_cmd = input()

print(f"Cupid's last position was {current_position}.")
print(was_successfull(neighborhood))
