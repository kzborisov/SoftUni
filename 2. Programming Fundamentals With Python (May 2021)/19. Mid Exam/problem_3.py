price_ratings = [int(x) for x in input().split(', ')]
entry_point = int(input())
items_type = input()

left = price_ratings[:entry_point]
right = price_ratings[entry_point+1:]

if items_type == "expensive":
    left = [x for x in left if x >= price_ratings[entry_point]]
    right = [x for x in right if x >= price_ratings[entry_point]]
elif items_type == "cheap":
    left = [x for x in left if x < price_ratings[entry_point]]
    right = [x for x in right if x < price_ratings[entry_point]]

if sum(left) >= sum(right):
    print(f"Left - {sum(left)}")
else:
    print(f"Right - {sum(right)}")
