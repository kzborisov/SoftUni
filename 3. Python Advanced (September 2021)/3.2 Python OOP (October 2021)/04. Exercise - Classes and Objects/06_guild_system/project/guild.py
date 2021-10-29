from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if not player.guild == Player.unaffiliated:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.unaffiliated
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        msg = f"Guild: {self.name}\n"
        msg += "\n".join([player.player_info() for player in self.players])
        return msg
