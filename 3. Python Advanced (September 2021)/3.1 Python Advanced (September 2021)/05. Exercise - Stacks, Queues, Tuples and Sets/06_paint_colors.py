from collections import deque

input_string = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
collected_colors = []

while input_string:
    left = input_string.popleft()
    right = input_string.pop() if input_string else ""
    color = left + right

    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue
    color = right + left
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        left = left[:-1]
        right = right[:-1]
        index = len(input_string) // 2
        if left:
            input_string.insert(index, left)
        if right:
            input_string.insert(index, right)


secondary_required_color = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow'],
}

for color in collected_colors:
    if color in main_colors:
        continue
    required_colors = secondary_required_color[color]
    is_valid = all([x in collected_colors for x in required_colors])
    if not is_valid:
        collected_colors.remove(color)


print(collected_colors)

