# Task 05. Numbers Filter
n = int(input())

positive = []
negative = []
even = []
odd = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    elif num % 2 == 1:
        odd.append(num)

    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

category = input()
categories = {
    'positive': positive,
    'negative': negative,
    'even': even,
    'odd': odd
}

try:
    print(categories[category])
except KeyError as e:
    print('Invalid category')
