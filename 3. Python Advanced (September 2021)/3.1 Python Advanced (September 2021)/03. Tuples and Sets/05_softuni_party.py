n = int(input())
guest_list = {input() for _ in range(n)}

while True:
    command = input()
    if command == "END":
        break
    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


print(len(guest_list))
vip_guest = sorted([guest for guest in guest_list if is_vip(guest)])
regular_guest = sorted([guest for guest in guest_list if not is_vip(guest)])

[print(g) for g in vip_guest]
[print(g) for g in regular_guest]
