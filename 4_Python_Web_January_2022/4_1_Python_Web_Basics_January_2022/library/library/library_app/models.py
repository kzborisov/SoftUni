from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(
        max_length=30,
    )
