# Task 04. Search
n = int(input())
word = input()

strings_list = []

for i in range(n):
    some_string = input()
    strings_list.append(some_string)


filtered = [x for x in strings_list if word in x]
print(strings_list)
print(filtered)
