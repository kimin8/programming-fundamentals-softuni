nums = list(map(int, input().split(", ")))

# [1, 2, 3, 4]
indices = []

for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
        indices.append(i)

print(indices)