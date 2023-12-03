capacity = int(input())
command = input()

users = {}

while command != "Statistics":

    tokens = command.split("=")
    instruction = tokens[0]

    if instruction == "Add":
        name = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])
        total_messages = sent + received
        
        if not name in users.keys():
            users[name] = total_messages

    elif instruction == "Message":
        sender = tokens[1]
        receiver = tokens[2]

        if (sender in users.keys()) and (receiver in users.keys()):
            users[sender] += 1
            users[receiver] += 1

            if users[sender] == capacity:
                del users[sender]
                print(f"{sender} reached the capacity!")

            if users[receiver] == capacity:
                del users[receiver]
                print(f"{receiver} reached the capacity!")

    elif instruction == "Empty":
        username = tokens[1]

        if username == "All":
            users.clear()
        else:
            if users[username]:
                del users[username]

    command = input()

count = len(users)

print(f"Users count: {count}")

for user in users.keys():
    print(f"{user} - {users[user]}")