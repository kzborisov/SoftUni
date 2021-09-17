text = input()
occurrences = {}

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 0
    occurrences[ch] += 1

{print(f"{ch}: {times} time/s") for ch, times in sorted(occurrences.items())}
