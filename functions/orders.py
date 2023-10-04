user_input = input()
quantity = int(input())

def return_price(product, count):
    if product == "coffee":
        return f"{1.5 * count:.2f}"
    elif product == "coke":
        return f"{1.4 * count:.2f}"
    elif product == "water":
        return f"{count:.2f}"
    elif product == "snacks":
        return f"{2 * count:.2f}"
    
print(return_price(user_input, quantity))