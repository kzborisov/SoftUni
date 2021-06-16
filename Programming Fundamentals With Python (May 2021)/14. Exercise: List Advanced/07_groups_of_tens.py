# Taks 07. Groups of tens
initial_group = list(map(int, input().split(", ")))
group = 10

while len(initial_group) > 0:
    list_of_numbers = [x for x in initial_group if x <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    initial_group = [x for x in initial_group if x not in list_of_numbers]
    list_of_numbers = []
    group += 10

