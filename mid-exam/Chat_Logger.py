user_input = input()
chat = []

while user_input != "end":
    user_input = user_input.split(" ")
    command = user_input[0]

    if command == "Chat":
        chat.append(user_input[1])

    elif command == "Delete":
        if user_input[1] in chat:
            chat.remove(user_input[1])
    
    elif command == "Edit":
        if user_input[1] in chat:
            target = chat.index(user_input[1])
            chat[target] = user_input[2]
        
    elif command == "Pin":
        if user_input[1] in chat:
            chat.remove(user_input[1])
            chat.append(user_input[1])

    elif command == "Spam":
        chat += user_input[1:]
    
    user_input = input()

for message in chat:
    print(message)