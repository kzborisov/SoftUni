from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        # Alone room has only one member
        super().__init__(family_name, pension, 1)
        self.room_cost = 10
