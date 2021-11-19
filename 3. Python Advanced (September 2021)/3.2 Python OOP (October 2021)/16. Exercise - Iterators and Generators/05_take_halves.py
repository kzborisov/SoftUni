def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))

        return result
    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
"""ou are given a skeleton with the following code:

Implement the three generator functions:
    • integers() - generates an infinite amount of integers (starting from 1)
    • halves() - generates the halves of those integers (each integer / 2)
    • take(n, seq) - takes the first n halves of those integers
Note: Complete the functionality in the skeleton and submit it to the judge system
Examples"""
