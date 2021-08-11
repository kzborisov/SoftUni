text = input().split()
result = ""
for word in text:
    result += word * len(word)

print(result)
