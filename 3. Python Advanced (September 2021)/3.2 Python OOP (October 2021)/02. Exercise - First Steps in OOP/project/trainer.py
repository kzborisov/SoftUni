from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for current_pokemon in self.pokemons:
            if current_pokemon.name == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n"
        data += "\n".join([f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons])
        return data
