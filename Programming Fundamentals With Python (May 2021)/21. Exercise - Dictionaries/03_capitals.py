countries = input().split(", ")
capitals = input().split(", ")

{print(f"{k} -> {v}") for k, v in dict(zip(countries, capitals)).items()}
