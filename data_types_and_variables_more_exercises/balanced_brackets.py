x = int(input())

isBalanced = True
isUnbalaned = False

for i in range(x):
    user_input = input()

    if isBalanced == False and user_input == "(" or isBalanced == True and user_input == ")":
       isUnbalaned = True

    if user_input == "(":
        isBalanced = False
    elif user_input == ")":
        isBalanced = True

if isUnbalaned:
    print("UNBALANCED")
else:
    if isBalanced:
        print("BALANCED")
    else:
        print("UNBALANCED")