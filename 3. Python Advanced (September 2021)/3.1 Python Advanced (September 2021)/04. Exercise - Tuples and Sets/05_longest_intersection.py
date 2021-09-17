n = int(input())
longest_intersection = []

for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    first_set = {x for x in range(first_start, first_end + 1)}
    second_set = {x for x in range(second_start, second_end + 1)}
    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
