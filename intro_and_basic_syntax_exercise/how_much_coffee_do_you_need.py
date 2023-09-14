user_input = input()
coffee_count = 0;

while user_input != "END":
    if user_input == "CODING" or user_input == "CAT" or user_input == "DOG" or user_input == "MOVIE":
        coffee_count += 2
    elif user_input == "coding" or user_input == "cat" or user_input == "dog" or user_input == "movie":
        coffee_count += 1

    if coffee_count > 5:
        print("You need extra sleep")
        break;
    user_input = input()
else:
    print(coffee_count)