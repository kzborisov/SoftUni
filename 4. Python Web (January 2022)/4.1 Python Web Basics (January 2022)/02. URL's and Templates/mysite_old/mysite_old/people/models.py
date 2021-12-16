from django.db import models

# Create your models here.
from django.forms import CharField, IntegerField


class People(models.Model):
    name = CharField(max_length=30)
    age = IntegerField()
