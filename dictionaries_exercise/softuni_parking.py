parking_lot = {}

n = int(input())

for i in range(n):

    user_input = input().split(" ")

    if user_input[0] == "register":
        command, username, plate_number = user_input
        if username in parking_lot.keys():
            print(f"ERROR: already registered with plate number {plate_number}")
        else:
            parking_lot[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    else:
        command, username = user_input
        if username in parking_lot.keys():
            del parking_lot[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for user in parking_lot.keys():
    print(f"{user} => {parking_lot[user]}")