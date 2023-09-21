n = int(input())
capacity = 255
filled = 0

for i in range(n):
    curr = int(input())
    if filled + curr <= capacity:
        filled += curr
    else:
        print("Insufficient capacity!")

print(filled)