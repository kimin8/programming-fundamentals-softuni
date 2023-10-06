password_attempt = input()

def validate(attempt:str) -> bool:
    isOk = True
    wrong_symbol = False
    digitsCount = 0

    if len(attempt) < 6 or len(attempt) > 10:
        print("Password must be between 6 and 10 characters")
        isOk = False

    for index in range(0, len(attempt)):
        letter = attempt[index]
        code = ord(letter)

        if (code >= 48 and code <= 57) or (code >= 65 and code <= 90) or (code >= 97 and code <= 122):
            pass
        else:
            wrong_symbol = True

    if wrong_symbol == True:
        print("Password must consist only of letters and digits")
        isOk = False
    
    for index in range(0, len(attempt)):
        letter = attempt[index]
        code = ord(letter)

        if code >= 48 and code <= 57:
            digitsCount += 1

    if digitsCount < 2:
        print("Password must have at least 2 digits")
        isOk = False

    return isOk

if validate(password_attempt) == True:
    print("Password is valid")