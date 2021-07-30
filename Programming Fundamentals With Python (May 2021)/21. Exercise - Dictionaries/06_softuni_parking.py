def register(parking_dict, username, license_plate):
    if username in parking_dict:
        print(f"ERROR: already registered with plate number {parking_dict[username]}")
    else:
        parking_dict[username] = license_plate
        print(f"{username} registered {license_plate} successfully")


def unregister(parking_dict, username):
    if username not in parking_dict:
        print(f"ERROR: user {username} not found")
    else:
        parking_dict.pop(username)
        print(f"{username} unregistered successfully")


parking = {}
n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "register":
        user, plate = cmd[1], cmd[2]
        register(parking, user, plate)
    elif cmd[0] == "unregister":
        user = cmd[1]
        unregister(parking, user)

for k, v in parking.items():
    print(f"{k} => {v}")