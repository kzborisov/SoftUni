n = int(input())
integers = []

for _ in range(n):
    curr_int = int(input())
    integers.append(curr_int)

cmd = input()


if cmd == 'positive':
    result = [x for x in integers if x >= 0]
elif cmd == 'negative':
    result = [x for x in integers if x < 0]
elif cmd == 'even':
    result = [x for x in integers if x % 2 == 0]
elif cmd == 'odd':
    result = [x for x in integers if x % 2 == 1]

print(result)