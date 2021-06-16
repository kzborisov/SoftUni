# Task 01. Which Are In

first_str = input().split(", ")
second_str = input().split(", ")

result = [x for x in first_str if any(x in xs for xs in second_str)]
print(result)
