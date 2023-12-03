import re

pattern = r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$"

def checkAttempt(regex, string):
    match = re.fullmatch(regex, string)
    if match:
        return True
    else:
        print(f"Try another password!")
        return False 
    

num = int(input())

for _ in range(num):
    attempt = input()

    isValid = checkAttempt(pattern, attempt)

    if isValid:
        final = ""
        groups = re.findall(pattern, attempt)
        for i in range(1, len(groups[0])):
            final += groups[0][i]
        print(f"Password: {final}")