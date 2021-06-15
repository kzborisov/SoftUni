# Task 01. No Vowels

def stringify(collection, sep):
    return sep.join(collection)


word = input()
vowels = [ 'a', 'o', 'u', 'e', 'i']
no_vowels = [x for x in word if x.lower() not in vowels]
print(stringify(no_vowels, ''))
