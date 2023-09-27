n = int(input())
word = input()
strings = []

for i in range(n):
    user_inp = input()
    strings.append(user_inp)

print(strings)

for i in range(len(strings) - 1, -1, -1):
    curr = strings[i]
    if word not in curr:
        strings.remove(curr)

print(strings)
