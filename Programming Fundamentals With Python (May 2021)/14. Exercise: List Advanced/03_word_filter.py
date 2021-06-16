# Task 03. Word Filter

input_string = input().split()

result = [x for x in input_string if len(x) % 2 == 0]
print("\n".join(result))
