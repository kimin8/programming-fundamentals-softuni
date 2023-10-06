number = int(input())

def sums_of_digits(a:int) -> str:
    temp = a
    even = 0
    odd = 0

    length_of_num = len(str(temp))

    for _ in range(length_of_num):
        digit = temp % 10

        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
        temp //= 10

    return f"Odd sum = {odd}, Even sum = {even}"

print(sums_of_digits(number))