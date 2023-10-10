from math import floor

def getDistance(x, y):
    diffX = abs(0 - x)
    diffY = abs(0 - y)

    return diffX + diffY


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first = getDistance(x1, y1)
second = getDistance(x2, y2)

if first < second or first == second:
    print(f"({floor(x1)}, {floor(y1)})")
elif first > second:
    print(f"({floor(x2)}, {floor(y2)})")