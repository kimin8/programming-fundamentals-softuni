budget = float(input())

colored_eggs = 0
breads = 0

kilo_flour = float(input())
pack_eggs = 0.75 * kilo_flour
liter_milk = 1.25 * kilo_flour

bread_price = kilo_flour + pack_eggs + liter_milk / 4

while True:

    if budget >= bread_price:
        budget -= bread_price
        breads += 1
        colored_eggs += 3
    else:
        break

    if breads % 3 == 0:
        colored_eggs -= breads - 2

print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")