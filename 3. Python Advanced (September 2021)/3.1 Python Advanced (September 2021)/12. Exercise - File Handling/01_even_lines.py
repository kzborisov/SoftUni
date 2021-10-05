chars = ["-", ",", ".", "!", "?"]
result = []

with open("text.txt", "r") as f:
    content = f.readlines()
    for index, line in enumerate(content):
        if index % 2 == 0:
            result.append(line.split())


for index in range(len(result)):
    line = result[index]

    for word_index in range(len(line)):
        for ch in chars:
            if ch in line[word_index]:
                line[word_index] = line[word_index].replace(ch, "@")

[print(*x[::-1]) for x in result]



