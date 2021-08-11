text = input().split()
occurrences = {}

for word in text:
    for ch in word:
        if ch not in occurrences:
            occurrences[ch] = 1
        else:
            occurrences[ch] += 1

[print(f"{k} -> {v}") for k, v in occurrences.items()]
