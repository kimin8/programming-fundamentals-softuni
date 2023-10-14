wagons_count = int(input())

wagons = [0 for _ in range(wagons_count)]

user_input = input()

while user_input != "End":
    parts = user_input.split(" ")

    command = parts[0]

    if command == "add":
        people = int(parts[1])
        wagons[len(wagons)-1] += people

    elif command == "insert":
        index = int(parts[1])
        people = int(parts[2])

        wagons[index] += people

    elif command == "leave":
        index = int(parts[1])
        people = int(parts[2])

        wagons[index] -= people

    user_input = input()
    
print(wagons)