words = {}
answer = []

sequence = input().split(" ")

for word in sequence:
    if word.lower() in words.keys():
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1

for el in words.keys():
    if words[el] % 2 != 0:
        answer.append(el)

print(" ".join(answer))