sequence = input().split(", ")

def check_if_palindrome(x):
    if int(x) < 0:
        print(False)
    else:
        if x == x[::-1]:
            print(True)
        else:
            print(False)

for element in sequence:
    check_if_palindrome(element)