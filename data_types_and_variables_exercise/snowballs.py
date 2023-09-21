import sys

snowball_count = int(input())

best_v = -sys.maxsize - 1
best_w = 0
best_t = 0
best_q = 0

for snowball in range(snowball_count):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    curr_value = (weight / time_needed) ** quality

    if curr_value > best_v:
        best_v = curr_value
        best_w = weight
        best_t = time_needed
        best_q = quality

print(f"{best_w} : {best_t} = {best_v:.0f} ({best_q})")