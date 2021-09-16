stack_input = list(input())
result = list()
while stack_input:
    result.append(stack_input.pop())
print(*result, sep="")
