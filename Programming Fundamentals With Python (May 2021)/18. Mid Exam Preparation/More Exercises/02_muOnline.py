"""
You have initial health 100 and initial bitcoins 0.
You will be given a string, representing the dungeons rooms.
Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space.

The command can be:
    • "potion"
        ◦ You are healed with the number in the second part.
            But your health cannot exceed your initial health (100).
        ◦ First print: "You healed for {amount} hp.".
        ◦ After that, print your current health: "Current health: {health} hp.".
    • "chest"
        ◦ You've found some bitcoins, the number in the second part.
        ◦ Print: "You found {amount} bitcoins."
    • In any other case you are facing a monster, you are going to fight.
            The second part of the room, contains the attack of the monster.
            You should remove the monster's attack from your health.
        ◦ If you are not dead (health <= 0) you've slain the monster, and you should print ("You slayed {monster}.")
        ◦ If you've died, print "You died! Killed by {monster}." and your quest is over.
            Print the best room you`ve manage to reach: "Best room: {room}".
If you managed to go through all the rooms in the dungeon, print on the next three lines:
"You've made it!", "Bitcoins: {bitcoins}", "Health: {health}".

Input / Constraints
You receive a string, representing the dungeons rooms,
separated with '|' (vertical bar): "room1|room2|room3…".

Test Input
rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000
cat 10|potion 30|orc 10|chest 10|snake 25|chest 110

Output
Print the corresponding messages, described above.
"""
import sys


def potion_cmd(hp, healing_pts):
    if hp + healing_pts > 100:
        healing_pts = 100 - hp
    hp += healing_pts
    print(f"You healed for {healing_pts} hp.")
    return hp


def chest_cmd(initial_bitcoins, bitcoins_found):
    print(f"You found {bitcoins_found} bitcoins.")
    return initial_bitcoins + bitcoins_found


def fight(hp, room_num, monster, attack_power):
    hp -= attack_power
    if hp > 0:
        print(f"You slayed {monster}.")
        return hp
    print(f"You died! Killed by {monster}.")
    print(f"Best room: {room_num+1}")
    sys.exit()


dungeon_rooms = input().split("|")
health = 100
bitcoins = 0


for idx, room in enumerate(dungeon_rooms):
    command = room.split()[0]
    number = int(room.split()[1])
    if command == "potion":
        health = potion_cmd(health, number)
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins = chest_cmd(bitcoins, number)
    else:
        health = fight(health, idx, command, number)

if health > 0:
    final_msg = f"You've made it!\n"\
                f"Bitcoins: {bitcoins}\n"\
                f"Health: {health}"
    print(final_msg)
