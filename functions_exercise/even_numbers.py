sequence = input().split(" ")
numbers = []

for el in sequence:
    numbers.append(int(el))

isEven = lambda x: x % 2 == 0

numbers = list(filter(isEven, numbers))

print(numbers)