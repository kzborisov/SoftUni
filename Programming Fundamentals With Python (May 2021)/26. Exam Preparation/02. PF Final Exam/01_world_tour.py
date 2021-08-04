def valid_index(initial_stops, idx):
    if idx in range(len(initial_stops)):
        return True
    return False


def add_stop(initial_stops, idx, string):
    if valid_index(initial_stops, idx):
        initial_stops = initial_stops[:idx] + string + initial_stops[idx:]
    return initial_stops


def remove_stop(initial_stops, start_idx, end_idx):
    if valid_index(initial_stops, start_idx) and valid_index(initial_stops, end_idx):
        substring = initial_stops[start_idx:end_idx+1]
        initial_stops = initial_stops.replace(substring, "", 1)
    return initial_stops


def switch(initial_stops, old_string, new_string):
    if old_string in initial_stops:
        initial_stops = initial_stops.replace(old_string, new_string)
    return initial_stops


stops = input()
command = input()

while not command == "Travel":
    cmd = command.split(":")

    if cmd[0] == "Add Stop":
        curr_idx, curr_string = cmd[1:]
        stops = add_stop(stops, int(curr_idx), curr_string)
    elif cmd[0] == "Remove Stop":
        curr_start_idx, curr_stop_idx = cmd[1:]
        stops = remove_stop(stops, int(curr_start_idx), int(curr_stop_idx))
    elif cmd[0] == "Switch":
        curr_old, curr_new = cmd[1:]
        stops = switch(stops, curr_old, curr_new)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
