import re

text = input()
pattern = r"([@#])(?P<word>[A-Za-z]{3,})(\1)(\1)(?P<mirror>[A-Za-z]{3,})(\1)"
matches = re.finditer(pattern, text)

matches = list(re.finditer(pattern, text))
mirror_words = [f"{match.group('word')} <=> {match.group('mirror')}"
                for match in matches if match.group('word') == match.group('mirror')[::-1]]

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
