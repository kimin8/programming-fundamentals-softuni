user_input = input()
stock = {}

while user_input != "statistics":
    collection = user_input.split(": ")
    key = collection[0]
    value = collection[1]

    if key in stock.keys():
        stock[key] += int(value)
    else:
        stock[key] = int(value)

    user_input = input()

print("Products in stock:")
for key in stock.keys():
    print(f"- {key}: {stock[key]}")

print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")