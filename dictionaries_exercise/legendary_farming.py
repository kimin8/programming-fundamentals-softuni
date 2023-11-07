items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

materials = input().split(" ")
finished = False

while not finished:

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        resource = materials[i + 1].lower()
    
        if resource in items.keys():
            items[resource] += quantity
        else:
            items[resource] = quantity
        
        if items["shards"] >= 250:
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            finished = True
            break

        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            print("Valanyr obtained!")
            finished = True
            break

        elif items["motes"] >= 250:
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            finished = True
            break

    else:
        materials = input().split(" ")

for item in items.keys():
    print(f"{item.lower()}: {items[item]}")