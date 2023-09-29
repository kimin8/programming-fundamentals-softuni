numbers = input()

nums_array = numbers.split(" ")
inverted = []
for num in nums_array:
    inverted.append(int(num) * -1)

print(inverted)