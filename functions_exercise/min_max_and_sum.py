sequence = input().split(" ")

numbers = []

for string in sequence:
    numbers.append(int(string))

print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")