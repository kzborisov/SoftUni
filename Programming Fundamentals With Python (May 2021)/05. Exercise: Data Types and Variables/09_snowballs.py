# Task 09. Snowballs
snowballs = int(input())
all_snowballs = []

for snowball in range(1, snowballs+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    snowball_dict = {
        'snow': snowball_snow,
        'time': snowball_time,
        'value': snowball_value,
        'quality': snowball_quality,
    }
    all_snowballs.append(snowball_dict)

best_value = 0
best_value_index = 0

for idx, snowball in enumerate(all_snowballs):
    if snowball['value'] >= best_value:
        best_value = snowball['value']
        best_value_index = idx

print(f"{all_snowballs[best_value_index]['snow']} : "
      f"{all_snowballs[best_value_index]['time']} = "
      f"{int(all_snowballs[best_value_index]['value'])} "
      f"({all_snowballs[best_value_index]['quality']})")
