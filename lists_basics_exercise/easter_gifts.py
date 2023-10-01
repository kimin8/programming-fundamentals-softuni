gifts_list = input().split(" ")
command = input()

while command != "No Money":

    components = command.split(" ")
    command_name = components[0]
    gift_name = components[1]

    if command_name == "OutOfStock":
        if gift_name in gifts_list:
            for i in range(len(gifts_list)-1, -1, -1):
                if gifts_list[i] == gift_name:
                    gifts_list[i] = "None"

    elif command_name == "Required":
        index = int(components[2])
        if index < len(gifts_list) and index > -1:
            gifts_list[index] = gift_name

    elif command_name == "JustInCase":
        gifts_list.pop()
        gifts_list.append(gift_name)

    command = input()

for j in range(len(gifts_list)-1, -1, -1):
    if gifts_list[j] == "None":
        gifts_list.pop(j)
    
print(" ".join(gifts_list))