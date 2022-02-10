from django.db import models

from ExpensesTracker.profiles.models import Profile


class Expense(models.Model):
    title = models.CharField(
        max_length=50,
    )
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

    @property
    def money_left(self):
        expenses = self.objects.all()
        print(expenses)
        return sum(e.price for e in expenses)
