def read_next(*args, **kwargs):
    for arg in args:
        for elem in arg:
            yield elem

    for item in kwargs.keys():
        yield item


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
