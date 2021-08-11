# Task 05. Word Synonyms
words_cnt = int(input())
synonyms = {}

for _ in range(words_cnt):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
