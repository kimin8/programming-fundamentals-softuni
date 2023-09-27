n = int(input())
numbers = []
filtered = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

for num in numbers:
    if command == "even":
        if num % 2 == 0:
            filtered.append(num)
    elif command == "odd":
        if num % 2 != 0:
            filtered.append(num)
    elif command == "negative":
        if num < 0:
            filtered.append(num)
    elif command == "positive":
        if num >= 0:
            filtered.append(num)

print(filtered)