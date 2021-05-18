# Task 04. More Exercises - Sum of a Beach
import sys

cmd = input()
events = ['coding', 'dog', 'cat', 'movie']

coffees = 0

while cmd != 'END':
    if cmd.lower() in events:
        if cmd.islower():
            coffees += 1
        elif cmd.isupper():
            coffees += 2

    cmd = input()

if coffees > 5:
    print('You need extra sleep')
    sys.exit()

print(coffees)
