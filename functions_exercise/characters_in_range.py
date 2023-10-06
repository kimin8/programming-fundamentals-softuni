first_char = input()
second_char = input()

def return_chars_between(a:str, b:str) -> list:
    list_of_chars = []

    for i in range(ord(a)+1, ord(b)):
        list_of_chars.append(chr(i))
    
    return list_of_chars

print(" ".join(return_chars_between(first_char, second_char)))