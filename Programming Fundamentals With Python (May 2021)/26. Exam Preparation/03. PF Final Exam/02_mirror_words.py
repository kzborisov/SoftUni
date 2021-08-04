import re


def is_palindrome(first, second):
    if first == second[::-1]:
        return True
    return False


text = input()
pattern = r"([@#])(?P<word>[A-Za-z]{3,})(\1)(\1)(?P<mirror>[A-Za-z]{3,})(\1)"
matches = re.finditer(pattern, text)
palindromes = {}
pairs = {}

for match in matches:
    word = match.group('word')
    mirror = match.group('mirror')
    pairs[word] = mirror
    if is_palindrome(word, mirror):
        palindromes[word] = mirror

if pairs:
    print(f"{len(pairs)} word pairs found!")
    if palindromes:
        print("The mirror words are:")
        result = ""
        for word, mirror in palindromes.items():
            result += f"{word} <=> {mirror}, "
        print(result[:-2])
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    if not palindromes:
        print("No mirror words!")
