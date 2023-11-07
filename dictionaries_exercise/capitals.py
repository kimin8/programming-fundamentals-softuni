countries = input().split(", ")
capitals = input().split(", ")

info = zip(countries, capitals)

world_map = {key:value for (key,value) in info}

for key in world_map.keys():
    print(f"{key} -> {world_map[key]}")