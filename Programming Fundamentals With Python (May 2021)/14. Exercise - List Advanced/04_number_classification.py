# Task 04. Number Classification

numbers = list(map(int, input().split(", ")))

positives, negatives, evens, odds = [], [], [], []
for x in numbers:
    positives.append(str(x)) if x >= 0 else negatives.append(str(x))
    evens.append(str(x)) if x % 2 == 0 else odds.append(str(x))

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")
