import re


def calc_coolnes(emoji):
    return sum([ord(x) for x in emoji])


def prod(digit_list):
    total = 1
    for digit in digit_list:
        total *= int(digit)
    return total


text = input()
digits = [int(x) for x in text if x.isdigit()]
cool_threshold = prod(digits)
pattern = r"([:]{2}|[*]{2})(?P<emoji>[A-Z][a-z]{2,})(\1)"
emojis = re.finditer(pattern, text)
all_emojis = {"all": [], "word": [], "cool": []}

for emoji in emojis:
    curr_emoji = emoji.group()
    all_emojis['all'].append(curr_emoji)
    word = emoji.group("emoji")
    all_emojis['word'].append(word)
    emoji_coolness = calc_coolnes(word)
    if emoji_coolness > cool_threshold:
        all_emojis['cool'].append(curr_emoji)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis['all'])} emojis found in the text. The cool ones are:")
[print(v) for v in all_emojis["cool"]]
