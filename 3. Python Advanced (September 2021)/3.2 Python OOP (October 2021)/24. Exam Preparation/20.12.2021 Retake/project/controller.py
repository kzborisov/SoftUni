class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player)

        return "Successfully added: " + ", ".join([p.name for p in added_players])

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ("Food", "Drink"):
            # Invalid sustenance type
            return

        player = self.__find_player(player_name)
        sustenances = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]

        if not sustenances:
            if sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            elif sustenance_type == "Drink":
                raise Exception("There are no drink supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply = sustenances.pop()
        self.supplies.reverse()
        self.supplies.remove(supply)
        self.supplies.reverse()

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)
        if first_player.stamina <= 0 and second_player.stamina > 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif first_player.stamina > 0 and second_player.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."
        elif first_player.stamina <= 0 and second_player.stamina <= 0:
            return "\n".join([f"Player {p.name} does not have enough stamina."
                              for p in [first_player, second_player]])

        # first_to_attack = sorted([first_player, second_player], key=lambda x: x.stamina)[0]
        if first_player.stamina < second_player.stamina:
            try:
                second_player.stamina -= (first_player.stamina * 0.5)
            except ValueError:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            try:
                first_player.stamina -= (second_player.stamina * 0.5)
            except ValueError:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"

        elif second_player.stamina < first_player.stamina:
            try:
                first_player.stamina -= (second_player.stamina * 0.5)
            except ValueError:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            try:
                second_player.stamina -= (first_player.stamina * 0.5)
            except ValueError:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"

        winner = sorted([first_player, second_player], key=lambda x: x.stamina)[-1]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            try:
                player.stamina -= player.age * 2
            except ValueError:
                player.stamina = 0

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
