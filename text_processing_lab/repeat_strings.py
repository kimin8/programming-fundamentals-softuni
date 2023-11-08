strings = input().split(" ")
repeated = [txt * len(txt) for txt in strings]
print("".join(repeated))