operator_input = input()
first_num = int(input())
second_num = int(input())

def solve(operator, a , b):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b

print(solve(operator_input, first_num, second_num))