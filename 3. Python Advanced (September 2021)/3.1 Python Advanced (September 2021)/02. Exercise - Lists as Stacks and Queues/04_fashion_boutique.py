box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
curr_rack_capacity = rack_capacity

while box_of_clothes:
    curr_cloth = box_of_clothes[-1]
    if curr_cloth > curr_rack_capacity:
        used_racks += 1
        curr_rack_capacity = rack_capacity
    else:
        curr_rack_capacity -= curr_cloth
        box_of_clothes.pop()

print(used_racks)
