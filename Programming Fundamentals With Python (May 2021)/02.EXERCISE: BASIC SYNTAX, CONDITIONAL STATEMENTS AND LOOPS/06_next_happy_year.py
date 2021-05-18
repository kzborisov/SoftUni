# Task 06. Next Happy Year

num = int(input()) + 1

while True:
    year = str(num)
    if len(set(year)) == len(year):
        print(year)
        break
    num += 1
