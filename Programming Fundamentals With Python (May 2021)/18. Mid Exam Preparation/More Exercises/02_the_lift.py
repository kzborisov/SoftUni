people_queue = int(input())
state = [int(x) for x in input().split()]

for idx in range(len(state)):
    while state[idx] < 4 and people_queue > 0:
        people_queue -= 1
        state[idx] += 1

if people_queue == 0 and not all(x == 4 for x in state):
    result = "The lift has empty spots!\n"
    result += f"{' '.join([str(x) for x in state])}"
elif people_queue > 0 and all(x == 4 for x in state):
    result = f"There isn't enough space! {people_queue} people in a queue!\n"
    result += f"{' '.join([str(x) for x in state])}"
else:
    result = f"{' '.join([str(x) for x in state])}"

print(result)
