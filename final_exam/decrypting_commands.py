starting = input()
command = input()

while command != 'Finish':
    
    tokens = command.split(" ")
    instruction = tokens[0]

    if instruction == "Replace":
        currentChar = tokens[1]
        newChar = tokens[2]

        starting = starting.replace(currentChar, newChar)
        print(starting)

    elif instruction == "Cut":
        startIndex = int(tokens[1])
        endIndex = int(tokens[2])

        if (startIndex >= 0 and startIndex < len(starting)) and (endIndex >= 0 and endIndex < len(starting)):
            starting = starting[:startIndex] + starting[endIndex+1:]
            print(starting)
        else:
            print("Invalid indices!")

    elif instruction == "Make":
        upper_or_lower = tokens[1]

        if upper_or_lower == "Upper":
            starting = starting.upper()
        else:
            starting = starting.lower()

        print(starting)

    elif instruction == "Check":
        to_check = tokens[1]

        if to_check in starting:
            print(f"Message contains {to_check}")
        else:
            print(f"Message doesn't contain {to_check}")

    elif instruction == "Sum":
        startIndex = int(tokens[1])
        endIndex = int(tokens[2])

        if (startIndex >= 0 and startIndex < len(starting)) and (endIndex >= 0 and endIndex < len(starting)):
            sum = 0

            for i in range(startIndex, endIndex + 1):
                sum += ord(starting[i])
            
            print(sum)
        
        else:
            print("Invalid indices!")

    command = input()