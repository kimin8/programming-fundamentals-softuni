from math import ceil

n = int(input())
p = int(input())

if not n % p == 0:
    print(ceil(n / p))
else:
    print(n // p)