# Task 08. Decipher This!
def ascii_to_char(word):
    first_letter = chr(int("".join([x for x in word if x.isdigit()])))
    text = "".join([x for x in word if not x .isdigit()])
    word = "".join(first_letter+text)
    return word


def replace_second_and_last(word):
    word_list = [x for x in word]
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    return "".join(word_list)


secret_msg = input().split()
secret_msg = list(map(lambda word: ascii_to_char(word), secret_msg))
secret_msg = list(map(lambda word: replace_second_and_last(word), secret_msg))
print(" ".join(secret_msg))
