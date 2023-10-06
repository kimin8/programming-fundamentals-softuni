a = int(input())
b = int(input())

def get_factorial(x:int) -> int:
    factorial = 1
    for i in range(x, 0, -1):
        factorial *= i
    
    return factorial

print(f"{get_factorial(a) / get_factorial(b):.2f}")