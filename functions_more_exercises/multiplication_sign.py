numbers = []

for _ in range(3):
    numbers.append(int(input()))

def getSign(list_of_nums):
    negative_count = 0

    if 0 in list_of_nums:
        return "zero"

    for num in list_of_nums:
        if num < 0:
            negative_count += 1
    
    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"
    
print(getSign(numbers))