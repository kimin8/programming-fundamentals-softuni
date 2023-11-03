collection = input().split(" ")
bakery = {}

for i in range(0, len(collection), 2):
    key = collection[i]
    value = collection[i + 1]
    bakery[key] = int(value)

print(bakery)