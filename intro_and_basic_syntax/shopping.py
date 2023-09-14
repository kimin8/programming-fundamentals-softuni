budget = int(input())

inp = input()
while inp != "End":
    buyings = int(inp)
    budget -= buyings

    if budget < 0:
        print("You went in overdraft!")
        break;
    else:
        inp = input()
else:
    print("You bought everything needed.")