user_input = input()

while user_input != "Welcome!":

    if user_input == "Voldemort":
        print("You must not speak of that name!")
        break;
    elif len(user_input) < 5:
        print(f"{user_input} goes to Gryffindor.")
    elif len(user_input) == 5:
        print(f"{user_input} goes to Slytherin.")
    elif len(user_input) == 6:
        print(f"{user_input} goes to Ravenclaw.")
    elif len(user_input) > 6:
        print(f"{user_input} goes to Hufflepuff.")
    user_input = input()
else:
    print("Welcome to Hogwarts.")