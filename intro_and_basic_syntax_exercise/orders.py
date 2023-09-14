n = int(input())
total_price = 0.0;

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule >= 0.01 and price_per_capsule <= 100 and days >= 1 and days <= 31 and capsules_per_day >= 1 and capsules_per_day <= 2000:
        price_for_coffee = days * capsules_per_day * price_per_capsule
        total_price += price_for_coffee

        print(f"The price for the coffee is: ${price_for_coffee:.2f}")

print(f"Total: ${total_price:.2f}")