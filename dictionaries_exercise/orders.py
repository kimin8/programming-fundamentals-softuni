order_dictionary = {}

user_input = input()

while user_input != "buy":
    product, price, quantity = user_input.split(" ")
    info = [float(price), int(quantity)]

    if product in order_dictionary.keys():
        order_dictionary[product][0] = float(price)
        order_dictionary[product][1] += int(quantity)
    else:
        order_dictionary[product] = info

    user_input = input()

for item in order_dictionary.keys():
    print(f"{item} -> {order_dictionary[item][0] * order_dictionary[item][1]:.2f}")