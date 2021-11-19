def fibonacci():
    x, y = 0, 1
    yield x
    while True:
        x, y = y, y + x
        yield x


generator = fibonacci()
for i in range(10):
    print(next(generator))
