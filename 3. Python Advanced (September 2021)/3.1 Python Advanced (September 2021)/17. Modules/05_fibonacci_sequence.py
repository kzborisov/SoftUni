from fibonacci import create_sequence, locate

print(create_sequence(10))
print(locate(13))

try:
    print(create_sequence(3))
    print(locate(10))
except IndexError as e:
    print(e)
