def cast_spell(hero, mana_needed, spell):
    hero_mana = heroes[hero][MANA_POINTS]
    if hero_mana >= mana_needed:
        heroes[hero][MANA_POINTS] -= mana_needed
        print(f"{hero} has successfully cast {spell} and now has {heroes[hero][MANA_POINTS]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def take_damage(hero, damage_pts, attacker):
    heroes[hero][HIT_POINTS] -= damage_pts
    if heroes[hero][HIT_POINTS] <= 0:
        print(f"{hero} has been killed by {attacker}!")
        heroes.pop(hero)
    else:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][HIT_POINTS]} HP left!")


def recharge(hero, mana_amount):
    if heroes[hero][MANA_POINTS] + mana_amount > MAX_MANA:
        mana_recharged = MAX_MANA - heroes[hero][MANA_POINTS]
        heroes[hero][MANA_POINTS] = MAX_MANA
    else:
        mana_recharged = (heroes[hero][MANA_POINTS] + mana_amount) - heroes[hero][MANA_POINTS]
        heroes[hero][MANA_POINTS] += mana_amount
    print(f"{hero} recharged for {mana_recharged} MP!")


def heal(hero, hp_amount):
    if heroes[hero][HIT_POINTS] + hp_amount > MAX_HEALTH:
        hp_healed = MAX_HEALTH - heroes[hero][HIT_POINTS]
        heroes[hero][HIT_POINTS] = MAX_HEALTH
    else:
        hp_healed = (heroes[hero][HIT_POINTS] + hp_amount) - heroes[hero][HIT_POINTS]
        heroes[hero][HIT_POINTS] += hp_amount
    print(f"{hero} healed for {hp_healed} HP!")


n = int(input())
heroes = {}
HIT_POINTS = "hit points"
MANA_POINTS = "mana points"
MAX_HEALTH = 100
MAX_MANA = 200
for _ in range(n):
    curr_hero, curr_hit_pts, curr_mana = input().split()
    heroes[curr_hero] = {HIT_POINTS: int(curr_hit_pts), MANA_POINTS: int(curr_mana)}

command = input()
while not command == "End":
    cmd = command.split(' - ')
    action = cmd[0]

    if action == "CastSpell":
        curr_hero, mana_pts_needed, spell_name = cmd[1:]
        cast_spell(curr_hero, int(mana_pts_needed), spell_name)
    elif action == "TakeDamage":
        curr_hero, damage, curr_attacker = cmd[1:]
        take_damage(curr_hero, int(damage), curr_attacker)
    elif action == "Recharge":
        curr_hero, mana = cmd[1:]
        recharge(curr_hero, int(mana))
    elif action == "Heal":
        curr_hero, hp = cmd[1:]
        heal(curr_hero, int(hp))

    command = input()

for hero_name, hero_info in sorted(heroes.items(), key=lambda kvp: (-kvp[1][HIT_POINTS], kvp[0])):
    print(hero_name)
    print(f"  HP: {hero_info[HIT_POINTS]}")
    print(f"  MP: {hero_info[MANA_POINTS]}")
