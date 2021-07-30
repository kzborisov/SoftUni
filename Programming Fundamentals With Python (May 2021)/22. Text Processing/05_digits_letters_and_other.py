text = input()
result = {"digits": "", "letters": "", "other": ""}

for ch in text:
    if ch.isdigit():
        result['digits'] += ch
    elif ch.isalpha():
        result['letters'] += ch
    else:
        result['other'] += ch

for k in result:
    print(result[k])
