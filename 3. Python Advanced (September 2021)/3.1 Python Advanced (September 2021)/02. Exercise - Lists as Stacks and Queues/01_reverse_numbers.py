n = [int(x) for x in input().split()]

stack = []
while n:
    stack.append(n.pop())

print(*stack)
