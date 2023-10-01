numbers_as_string = input().split(" ")
n = int(input())
numbers = []

for string in numbers_as_string:
    numbers.append(int(string))

sorted_numbers = sorted(numbers)
removed = sorted_numbers[0:n]

for num in removed:
    numbers.remove(num)

final = []

for el in numbers:
    final.append(str(el))

print(", ".join(final))