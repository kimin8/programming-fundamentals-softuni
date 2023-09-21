year = int(input()) + 1

while True:
    shouldPrint = True
    for i in range(0, 10):
        if str(year).count(str(i)) > 1:
            shouldPrint = False

    if shouldPrint:
        print(year)
        break;

    year += 1


