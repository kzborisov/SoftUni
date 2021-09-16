n = int(input())
stack = []

for _ in range(n):
    line_info = input().split()
    num = line_info[0]

    if num == "1":
        num_as_int = int(line_info[1])
        stack.append(num_as_int)
    elif num == "2":
        if stack:
            stack.pop()
    elif num == "3":
        if stack:
            print(max(stack))
    elif num == "4":
        if stack:
            print(min(stack))

result = []
while stack:
    result.append(stack.pop())

print(*result, sep=", ")
