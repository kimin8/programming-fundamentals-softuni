def round_the_numbers(sequence):
    list_of_rounded = []

    for number in sequence:
        list_of_rounded.append(round(float(number), None ))

    return list_of_rounded

non_rounded_sequence = input().split(" ")

print(round_the_numbers(non_rounded_sequence))