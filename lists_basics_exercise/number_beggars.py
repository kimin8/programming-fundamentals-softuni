integers = input().split(", ")
beggars = int(input())

sum_per_beggar = []
starter_index = 0

while starter_index < beggars:
    current_beggar_sum = 0
    for current_index in range(starter_index, len(integers), beggars):
        current_beggar_sum += int(integers[current_index])
    sum_per_beggar.append(current_beggar_sum)

    starter_index+=1

print(sum_per_beggar)