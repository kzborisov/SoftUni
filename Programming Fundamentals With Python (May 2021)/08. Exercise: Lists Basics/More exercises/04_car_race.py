# Task 04. More Exercises Car Race

def calculate_time(arr_input):
    time = 0
    for step in arr_input:
        if step == 0:
            time *= 0.8
        time += step
    return time


race = list(map(int, input().split()))
left = race[:len(race)//2]
right = race[(len(race)//2)+1:]
right.reverse()
left_time = calculate_time(left)
right_time = calculate_time(right)

if left_time <= right_time:
    winner = 'left'
    total_time = left_time
else:
    winner = 'right'
    total_time = right_time

print(f'The winner is {winner} with total time: {total_time:.1f}')
