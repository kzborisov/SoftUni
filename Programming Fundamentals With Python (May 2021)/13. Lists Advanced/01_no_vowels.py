# Task 01. No Vowels
word = input()
VOWELS = ['a', 'o', 'u', 'e', 'i']
no_vowels = [x for x in word if x.lower() not in VOWELS]
print(*no_vowels, sep="")