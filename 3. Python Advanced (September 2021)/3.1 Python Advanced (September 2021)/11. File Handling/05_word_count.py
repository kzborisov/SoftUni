with open("words.txt", "r") as f:
    words = f.readlines()[0].split()

words_found = {x: 0 for x in words}
with open("input.txt", 'r') as f:
    for num, line in enumerate(f, start=1):
        for word in words:
            if word in line:
                words_found[word] += 1

with open("output.txt", "w") as f:
    for word, count in sorted(words_found.items(), key=lambda x: -x[1]):
        f.write(f"{word} - {count}\n")
