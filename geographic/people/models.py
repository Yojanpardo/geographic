from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    born_date = models.DateField(auto_now=False)
    creation_day = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=30)
    nationalities = models.ManyToManyField('countries.Country')
