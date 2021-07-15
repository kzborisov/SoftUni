# Task 04. Odd Occurrences
words = input().split()
words_dict = {}

for word in words:
    word = word.lower()
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

[print(f"{key}", end=" ") for key in words_dict if not words_dict[key] % 2 == 0]
