sequence = input().split()
total_sum = 0

for elem in sequence:
    first_letter = elem[0]
    last_letter = elem[-1]
    num = int(elem[1:-1])
    curr_result = 0

    if first_letter.isupper():
        pos_in_alphabet = ord(first_letter) - 64
        curr_result += num / pos_in_alphabet
    elif first_letter.islower():
        pos_in_alphabet = ord(first_letter) - 96
        curr_result += num * pos_in_alphabet

    if last_letter.isupper():
        pos_in_alphabet = ord(last_letter) - 64
        curr_result -= pos_in_alphabet
    elif last_letter.islower():
        pos_in_alphabet = ord(last_letter) - 96
        curr_result += pos_in_alphabet

    total_sum += curr_result
print(f"{total_sum:.2f}")
