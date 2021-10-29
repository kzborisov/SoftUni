class Player:
    unaffiliated = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.unaffiliated

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        msg = f"Name: {self.name}\n"
        msg += f"Guild: {self.guild}\n"
        msg += f"HP: {self.hp}\n"
        msg += f"MP: {self.mp}\n"
        msg += "\n".join(
            [f"==={skill_name} - {mana_cost}"
             for skill_name, mana_cost in self.skills.items()])
        return msg
