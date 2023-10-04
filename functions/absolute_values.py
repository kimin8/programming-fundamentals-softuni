sequence = input().split(" ")

def convert_to_abs(seq):
    new_list = []
    
    for element in seq:
        new_list.append(abs(float(element)))
    
    return new_list

print(convert_to_abs(sequence))