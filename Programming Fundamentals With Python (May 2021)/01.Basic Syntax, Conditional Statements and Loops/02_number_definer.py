# Task 02. Number Definer

num = float(input())

if num == 0:
    result = 'zero'
elif num > 0:
    result = 'positive'
    if num < 1:
        result = 'small ' + result
    elif num > 1000000:
        result = 'large ' + result
else:
    result = 'negative'
    if num > -1:
        result = 'small ' + result
    elif num < -1000000:
        result = 'large ' + result

print(result)
