from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
    )

    last_name = models.CharField(
        max_length=15,
    )

    budget = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
