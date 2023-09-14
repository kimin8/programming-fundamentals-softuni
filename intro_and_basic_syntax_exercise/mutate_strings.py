string1 = input()
string2 = input()

current_string = string1

for i in range(len(string1)):
    if current_string[i] != string2[i]:
        current_string = current_string[:i] + string2[i] + current_string[i+1:]
        if current_string != string1:
            print(current_string)