inventory = {}

resource = input()

while resource != "stop":
    quantity = int(input())

    if resource in inventory.keys():
        inventory[resource] += quantity
    else:
        inventory[resource] = quantity

    resource = input()

for element in inventory.keys():
    print(f"{element} -> {inventory[element]}")