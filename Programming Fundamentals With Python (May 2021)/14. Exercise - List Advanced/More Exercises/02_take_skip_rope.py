# Task 02 More Exercises Take/Skip Rope

hidden_msg = input()
numbers = [int(x) for x in hidden_msg if x.isdigit()]
non_numbers = [x for x in hidden_msg if not x.isdigit()]
take_list = [numbers[x] for x in range(len(numbers)) if x % 2 == 0]
skip_list = [numbers[x] for x in range(len(numbers)) if not x % 2 == 0]


result = []
skipped = 0

for take, skip in zip(take_list, skip_list):
    result.append(non_numbers[:take])
    non_numbers = non_numbers[take+skip:]
    skipped += skip

print("".join([el for sublist in result for el in sublist]))