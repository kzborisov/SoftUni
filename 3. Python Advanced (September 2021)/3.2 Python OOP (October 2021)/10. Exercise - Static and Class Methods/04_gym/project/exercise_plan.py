class ExercisePlan:
    _id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        res = ExercisePlan._id
        ExercisePlan._id += 1
        return res

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
