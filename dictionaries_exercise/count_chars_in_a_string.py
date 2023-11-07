characters = {}

word = input()

for i in range(0, len(word)):
    letter = word[i]
    if letter != " ":
        if letter in characters.keys():
            characters[letter] += 1
        else:
            characters[letter] = 1

for element in characters.keys():
    print(f"{element} -> {characters[element]}")