from sys import maxsize

divisor = int(input())
boundary = int(input())

max_integer = -maxsize - 1

for i in range(boundary+1):
    if i % divisor == 0 and i > 0 and i <= boundary:
        if i > max_integer:
            max_integer = i

print(max_integer)