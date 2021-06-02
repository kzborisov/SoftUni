# Task 05. Faro Shuffle

def faro_shuffle(arr_input):
    left_half = deck[:len(arr_input) // 2]
    right_half = deck[len(arr_input) // 2:]
    new_list = []
    for ind in range(len(left_half)):
        new_list.append(right_half[ind])
        new_list.append(left_half[ind])
    return new_list


deck = input().split()
count = int(input())

first = [deck.pop(0)]
last = [deck.pop(len(deck)-1)]

for i in range(1, count+1):
    tmp = faro_shuffle(deck)
    deck = tmp

print(first+deck+last)
