collection_items = input().split("|")
budget = float(input())

TICKET_PRICE = 150
starting_money = budget
prices_list = []
temporary_money = 0

for item_info in collection_items:
    item_type, string_price = item_info.split("->")
    price = float(string_price)

    if budget >= price:
        if item_type == "Clothes":
            if price <= 50:
                budget -= price
                prices_list.append(f"{price*1.4:.2f}")
                temporary_money += price*1.4
        elif item_type == "Shoes":
            if price <= 35:
                budget -= price
                prices_list.append(f"{price*1.4:.2f}")
                temporary_money += price*1.4
        elif item_type == "Accessories":
            if price <= 20.50:
                budget -= price
                prices_list.append(f"{price*1.4:.2f}")
                temporary_money += price*1.4

print(" ".join(prices_list))
print(f"Profit: {temporary_money + budget - starting_money:.2f}")

if temporary_money + budget >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")