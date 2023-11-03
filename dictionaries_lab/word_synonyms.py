words = {}
n = int(input())

for _ in range(n):
    word = input()
    synonym = input()

    if word in words.keys():
        words[word].append(synonym)
    else:
        words[word] = [synonym]

for key in words.keys():
    print(f"{key} - {', '.join(words[key])}")