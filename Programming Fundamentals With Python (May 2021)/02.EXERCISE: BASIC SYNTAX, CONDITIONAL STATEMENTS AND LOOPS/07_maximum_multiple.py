# Task 07. Maximum Multiple

divisor = int(input())
bound = int(input())

for n in range(1, bound+1):
    if n % divisor == 0:
        largest = n

print(largest)
