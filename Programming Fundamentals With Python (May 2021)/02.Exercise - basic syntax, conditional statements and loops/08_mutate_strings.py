# Task 08. Mutate Strings

str_1 = input()
str_2 = input()

new_str = list(str_1)

for ch in range(len(str_2)):
    if new_str[ch] == str_2[ch]:
        continue
    else:
        new_str[ch] = str_2[ch]
    print(''.join(new_str))
