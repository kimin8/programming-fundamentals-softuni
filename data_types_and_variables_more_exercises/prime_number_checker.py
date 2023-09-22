x = int(input())

isPrime = True

if x > 1:
    for divisor in range(2, x):
        if x % divisor == 0:
            isPrime = False
else:
    isPrime = False

print(isPrime)