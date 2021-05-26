# Task 07. Maximum Multiple

divisor = int(input())
bound = int(input())
largest = 0
for n in range(divisor+1, bound+1):
    if n % divisor == 0:
        largest = n

print(largest)
