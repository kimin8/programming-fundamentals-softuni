n = int(input())

for i in range(0, n):
    x = int(input())
    if x % 2 != 0:
        print(f"{x} is odd!")
        break

else:
    print("All numbers are even.")

