from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @classmethod
    def validate_speed_limit(cls, value):
        if value < cls.MIN_SPEED_LIMIT or value > cls.MAX_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! "
                             f"Must be between {cls.MIN_SPEED_LIMIT} and {cls.MAX_SPEED_LIMIT}!")
