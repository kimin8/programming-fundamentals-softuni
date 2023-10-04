collection = input().split(", ")

for i in range(len(collection)-1,-1,-1):
    if int(collection[i]) == 0:
        collection.append(int(collection[i]))
        collection.pop(i)
    else:
        collection[i] = int(collection[i])

print(collection)