expression = [ch for ch in input().split()]

numbers_stack = []
operators = ["*", "+", "-", "/"]

for index, value in enumerate(expression):
    if value in operators:
        if value == "/":
            value = "//"

        result = value.join(numbers_stack)
        result = eval(result)
        numbers_stack = []
        numbers_stack.append(str(result))
        final_result = result
    else:
        numbers_stack.append(value)

print(numbers_stack[0])
