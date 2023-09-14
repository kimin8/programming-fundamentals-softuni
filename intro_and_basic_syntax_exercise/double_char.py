user_input = input()

while user_input != "End":
    new_string = ""

    if user_input != "SoftUni":
        for i in range(0, len(user_input)):
            new_string += f"{user_input[i]}{user_input[i]}"

        print(new_string)

    user_input = input()
