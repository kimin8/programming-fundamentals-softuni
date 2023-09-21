n = int(input())

for number in range(1, n + 1):
    isSpecial = False
    temp = number
    sum = 0

    for i in range(0, len(str(number))):
        digit = temp % 10
        temp //= 10
        sum += digit

    if sum == 5 or sum == 7 or sum == 11:
        isSpecial = True

    print(f"{number} -> {isSpecial}")