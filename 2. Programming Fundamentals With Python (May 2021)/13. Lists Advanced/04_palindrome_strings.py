# Task 04 Palindrome Strings
text = input().split()
palindrome = input()

palindromes = [x for x in text if x == x[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")
