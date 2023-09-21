lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

ans = 0
shield_broken = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        ans += helmet_price
    if fight % 3 == 0:
        ans += sword_price
        if fight % 2 == 0:
            ans += shield_price
            shield_broken += 1
            if shield_broken % 2 == 0 and shield_broken > 0:
                ans += armor_price

print(f"Gladiator expenses: {ans:.2f} aureus")