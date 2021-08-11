# Task 06. Triples of Latin Letters
letters = int(input())

for i in range(letters):
    for j in range(letters):
        for k in range(letters):
            print(f'{chr(97+i)}{chr(97+j)}{chr(97+k)}')
