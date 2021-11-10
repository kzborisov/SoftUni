import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id, name, date, age_restriction):
        creation_day, creation_month, creation_year = [int(x) for x in date.split(".")]
        datetime_object = datetime.datetime.strptime(str(creation_month), "%m")
        month_name = datetime_object.strftime("%B")
        return cls(name, dvd_id, creation_year, month_name, age_restriction)

    def get_status(self):
        return "rented" if self.is_rented else "not rented"

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {self.get_status()}"
