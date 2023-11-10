def get_position_lower(letter):
    return ord(letter) - 96

def get_position_upper(letter):
    return ord(letter) - 64

sequence = input().split()
final_sum = 0

for item in sequence:
    first_letter = item[0]
    number = int(item[1:len(item)-1])
    second_letter = item[len(item)-1]

    resulting_number = 0

    if first_letter.isupper():
        resulting_number = number / get_position_upper(first_letter)
    else:
        resulting_number = number * get_position_lower(first_letter)
    
    if second_letter.isupper():
        resulting_number -= get_position_upper(second_letter)
    else:
        resulting_number += get_position_lower(second_letter)

    final_sum += resulting_number

print(f"{final_sum:.2f}")