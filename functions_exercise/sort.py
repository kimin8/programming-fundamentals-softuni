sequence = input().split(" ")
numbers = []

for num_as_str in sequence:
    numbers.append(int(num_as_str))

print(sorted(numbers))