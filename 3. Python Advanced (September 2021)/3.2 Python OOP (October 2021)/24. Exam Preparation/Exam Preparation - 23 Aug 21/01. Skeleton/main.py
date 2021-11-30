from project.space_station import SpaceStation

station = SpaceStation()
print(station.add_astronaut("Biologist", "Pesho"))
print(station.add_astronaut("Geodesist", "Pesho2"))
print(station.add_astronaut("Meteorologist", "Pesho3"))

print(station.add_planet("Mars", "rock1, rock2"))

print(station.send_on_mission("Mars"))
print(station.report())
