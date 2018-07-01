from django.db import models

# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=20,unique=True)
    population = models.PositiveIntegerField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
