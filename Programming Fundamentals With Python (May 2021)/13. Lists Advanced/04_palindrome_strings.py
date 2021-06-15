# Task 04 Palindrom Strings

def check_palindrome(word):
    if word == word[::-1]:
        return True
    return False


text = input().split()
palindrome = input()


palindromes = [x for x in text if check_palindrome(x)]
found_palindromes = [x for x in palindromes if x == palindrome]

print(palindromes)
print(f"Found palindrome {len(found_palindromes)} times")
