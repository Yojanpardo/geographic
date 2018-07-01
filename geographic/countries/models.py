from django.db import models

# Create your models here.

class Country(models.Model):
    CLASSIFICATION=(
        ('A','Safe'),
        ('B','Less safe'),
        ('C','Unsafe'),
        ('D','More Unsafe'),
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    description = models.TextField(max_length=255)
    classification = models.CharField(max_length=1,choices=CLASSIFICATION,default='C')
    continent = models.ForeignKey('continents.Continent',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
