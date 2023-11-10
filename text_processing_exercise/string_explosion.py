message = input()
result = ""
strength = 0

for index in range(len(message)):
    if strength > 0 and message[index] != ">":
        strength -= 1
    elif message[index] == ">":
        result += message[index]
        strength += int(message[index + 1])
    else:
        result += message[index]

print(result)