import re

n = int(input())
pattern = r"\|"\
          r"(?P<name>[A-Z]{4,})"\
          r"\|\:#"\
          r"(?P<title>[A-Za-z]+\s[A-Za-z]+)\#"

for _ in range(n):
    boss = input()
    match = re.match(pattern, boss)
    if not match:
        print("Access denied!")
        continue

    boss_name = match.group("name")
    boss_title = match.group("title")
    print(f"{boss_name}, The {boss_title}")
    print(f">> Strength: {len(boss_name)}")
    print(f">> Armor: {len(boss_title)}")
