factor = int(input())
count = int(input())

multiples = list(range(1, count + 1))
l_to_print = []
for num in multiples:
    l_to_print.append(num * factor)

print(l_to_print)