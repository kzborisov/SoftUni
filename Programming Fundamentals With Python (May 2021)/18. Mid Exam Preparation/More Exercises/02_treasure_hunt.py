loot = input().split("|")
cmd = input()


class Treasure:
    def __init__(self, loot):
        self.loot = loot

    def loot_items(self, found_treasure):
        for item in found_treasure:
            if item not in self.loot:
                self.loot.insert(0, item)

    def drop(self, idx):
        if idx in range(len(self.loot)):
            self.loot.append(self.loot.pop(idx))

    def steal(self, count):
        if count > len(self.loot):
            count = len(self.loot)

        stolen = []
        for _ in range(count):
            stolen.append(self.loot.pop())
        print(', '.join(reversed(stolen)))

    def __repr__(self):
        if self.loot:
            gains = list(map(len, self.loot))
            average_gain = sum(gains) / len(self.loot)
            return f'Average treasure gain: {average_gain:.2f} pirate credits.'
        return 'Failed treasure hunt.'


treasure = Treasure(loot)

while not cmd == "Yohoho!":
    command = cmd.split()[0]
    if command == "Loot":
        items = cmd.split()[1:]
        treasure.loot_items(items)
    elif command == "Drop":
        loot_index = int(cmd.split()[1])
        treasure.drop(loot_index)
    elif command == "Steal":
        items_count = int(cmd.split()[1])
        treasure.steal(items_count)

    cmd = input()


print(treasure)
