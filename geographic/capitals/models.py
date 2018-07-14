from django.db import models

# Create your models here.

class Capital(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    country = models.OneToOneField('countries.Country',on_delete=models.CASCADE,related_name='city')
