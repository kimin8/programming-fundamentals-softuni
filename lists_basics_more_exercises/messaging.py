numbers_collection = input().split(" ")
encoded = input()
message = ""

for element in numbers_collection:
    number = int(element)
    temp = int(element)
    index = 0

    for i in range(len(element)):
        index += temp % 10
        temp //= 10
    
    while index >= len(encoded):
        index -= len(encoded)

    message += encoded[index]
    encoded = encoded[:index] + encoded[index + 1:]

print(message)