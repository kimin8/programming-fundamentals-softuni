collection = input().split(" ")
request = input().split(" ")

stock = {}

for i in range(0, len(collection), 2):
    key = collection[i]
    value = collection[i + 1]
    stock[key] = int(value)

for item in request:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")