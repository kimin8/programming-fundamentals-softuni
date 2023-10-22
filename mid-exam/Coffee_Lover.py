collection = input().split(" ")
n = int(input())

for _ in range(n):
    user_input = input().split(" ")

    command = user_input[0]

    if command == "Include":
        coffee = user_input[1]
        collection.append(coffee)
    
    elif command == "Remove":
        first_or_last = user_input[1]
        number_of_coffees = int(user_input[2])

        if len(collection) >= number_of_coffees:
            if first_or_last == "first":
                collection = collection[number_of_coffees:]
            elif first_or_last == "last":
                collection = collection[:len(collection) - number_of_coffees]

    elif command == "Prefer":
        first_index = int(user_input[1])
        second_index = int(user_input[2])

        if (first_index >= 0 and first_index < len(collection)) and (second_index >= 0 and second_index < len(collection)):
            collection[first_index], collection[second_index] = collection[second_index], collection[first_index]

    elif command == "Reverse":
        collection = list(reversed(collection))

print(f"Coffees:\n{' '.join(collection)}")