class Player:
    def __init__(self, friends):
        self.friends = friends

    def __repr__(self):
        blacklisted = [x for x in self.friends if x == "Blacklisted"]
        lost = [x for x in self.friends if x == "Lost"]
        return f"Blacklisted names: {len(blacklisted)}\n" \
               f"Lost names: {len(lost)}\n"\
               f"{' '.join(self.friends)}"

    def __is_name_present(self, name):
        return True if name in self.friends else False

    def __is_index_valid(self, idx):
        return True if idx in range(len(self.friends)) else False

    def blacklisted(self, name):
        if self.__is_name_present(name):
            self.friends[self.friends.index(name)] = "Blacklisted"
            return f"{name} was blacklisted."
        return f"{name} was not found."

    def error(self, idx):
        if self.__is_index_valid(idx):
            if self.friends[idx] not in ["Blacklisted", "Lost"]:
                name = self.friends[idx]
                self.friends[idx] = "Lost"
                print(f"{name} was lost due to an error.")

    def change(self, idx, new_name):
        if self.__is_index_valid(idx):
            old_name = self.friends[idx]
            self.friends[idx] = new_name
            print(f"{old_name} changed his username to {self.friends[idx]}.")


friends_list = input().split(", ")
command = input()
player = Player(friends_list)

while not command == "Report":
    cmd = command.split()[0]

    if cmd == "Blacklist":
        username = command.split()[1]
        print(player.blacklisted(username))
    elif cmd == "Error":
        name_idx = int(command.split()[1])
        player.error(name_idx)
    elif cmd == "Change":
        name_idx = int(command.split()[1])
        new_username = command.split()[2]
        player.change(name_idx, new_username)

    command = input()

print(player)
