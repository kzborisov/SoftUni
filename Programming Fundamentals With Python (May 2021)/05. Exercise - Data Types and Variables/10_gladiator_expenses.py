# Task 10. Gladiator Expenses
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmet = (lost_fights // 2) * helmet_price
sword = (lost_fights // 3) * sword_price
shield = lost_fights // 6
total_shield = (lost_fights // 6) * shield_price
armor = (shield // 2) * armor_price

result = helmet + sword + total_shield + armor
print(f'Gladiator expenses: {result:.2f} aureus')
