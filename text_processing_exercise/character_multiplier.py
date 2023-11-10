strings = input().split(" ")
total = 0

lowest_length = min(len(strings[0]), len(strings[1]))
first = strings[0][:lowest_length]
second = strings[1][:lowest_length]

for i in range(0, lowest_length):
    total += ord(strings[0][i]) * ord(strings[1][i])

if len(strings[0]) > len(strings[1]):

    first_end = strings[0][lowest_length:]

    for j in range(0, len(first_end)):
        total += ord(first_end[j])

elif len(strings[0]) < len(strings[1]):

    second_end = strings[1][lowest_length:]

    for k in range(0, len(second_end)):
        total += ord(second_end[k])

print(total)