with open("./numbers.txt", "r") as f:
    content = f.read()
    print(content)
    file_sum = sum(int(x) for x in content.split("\n"))

print(file_sum)
