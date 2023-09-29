cards = input().split()
times = int(input())

for j in range(times):
    half = len(cards) // 2
    left = cards[0:half]
    right = cards[half:]
    final_list = []
    for i in range(len(left)):
        final_list.append(left[i])
        final_list.append(right[i])
    cards = final_list

print(final_list)