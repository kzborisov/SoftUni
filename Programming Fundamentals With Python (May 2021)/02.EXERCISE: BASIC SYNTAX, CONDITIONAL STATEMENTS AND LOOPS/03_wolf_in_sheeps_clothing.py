# Task 03. More Exercises - Wolfs in Sheep's Clothing
herd = input().split(', ')[::-1]

for idx, sheep in enumerate(herd):
    if idx == 0 and sheep == 'wolf':
        print('Please go away and stop eating my sheep')
    elif sheep == 'wolf':
        print(f'Oi! Sheep number {idx}! You are about to be eaten by a wolf!')
