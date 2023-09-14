n = int(input())

for i in range(n):
    word = input()
    isPure = True

    for j in range(0, len(word)):

        if word[j] == ',' or word[j] == '.' or word[j] == '_':
            isPure = False

    if isPure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")