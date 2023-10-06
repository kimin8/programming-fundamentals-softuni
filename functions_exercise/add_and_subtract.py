def sum_numbers(a, b):
    return a+b

def subtract(a,b):
    return a-b

def add_and_subtract(a,b,c):
    d = sum_numbers(a,b)
    print(subtract(d, c))

first_num = int(input())
second_num = int(input())
third_num = int(input())

add_and_subtract(first_num, second_num, third_num)