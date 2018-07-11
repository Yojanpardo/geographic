from django.db import models
from colorful.fields import RGBColorField
# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=20,unique=True)
    population = models.PositiveIntegerField()
    color = RGBColorField()

    def __str__(self):
        return self.name
