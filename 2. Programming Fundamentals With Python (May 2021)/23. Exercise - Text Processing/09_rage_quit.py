import re

input_string = input().upper()

splitted_string = re.split(r"(\d+)", input_string)
result = ""

for i in range(0, len(splitted_string) - 1, 2):
    curr_string = splitted_string[i]
    reps = int(splitted_string[i+1])
    result += curr_string * reps

unique_chars = len(set(result))
print(f"Unique symbols used: {unique_chars}")
print(result)
