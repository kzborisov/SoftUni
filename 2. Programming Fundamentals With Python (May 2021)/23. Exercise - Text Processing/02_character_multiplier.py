def longer_word(str_1, str_2):
    return str_1 if len(str_1) > len(str_2) else str_2


word_one, word_two = input().split()
result = 0

shorter_len = min(len(word_one), len(word_two))
longer_len = max(len(word_one), len(word_two))
word = longer_word(word_one, word_two)

for i in range(shorter_len):
    result += ord(word_one[i]) * ord(word_two[i])

for i in range(shorter_len, longer_len):
    a = word[i]
    result += ord(word[i])

print(result)
