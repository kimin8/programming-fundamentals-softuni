message = input()
for i in range(0, len(message)):
    print(chr(ord(message[i])+3), end="")