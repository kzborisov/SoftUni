import re


def count_letters(text):
    return len(re.findall(r"[a-zA-Z]", text))


def count_punctuation(text):
    return len([x for x in text if x in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'])


lines = []

with open("text.txt", "r") as f:
    content = f.readlines()
    for index, line in enumerate(content):
        letters_count = count_letters(line)
        punctuation = count_punctuation(line)
        line = line.strip("\n")
        lines.append(f"Line {index + 1}: {line} ({letters_count})({punctuation})\n")

with open("output.txt", "w") as f:
    for line in lines:
        f.write(line)
