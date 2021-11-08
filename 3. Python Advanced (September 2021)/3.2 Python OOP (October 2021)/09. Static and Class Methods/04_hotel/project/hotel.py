class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = self.get_guests()

    def get_guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def _get_room_by_number(self, room_number):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        return possible_rooms[0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, guests_count):
        room = self._get_room_by_number(room_number)

        if room.take_room(guests_count):
            return

    def free_room(self, room_number):
        room = self._get_room_by_number(room_number)
        if room.free_room():
            return

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return (f"Hotel {self.name} has {self.get_guests()} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}")
