from django.db import models

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    born_date = models.DateField(auto_now=False)
    creation_day = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=30)
    nationalities = models.ManyToManyField('countries.Country')
    is_active = models.BooleanField(default=True)
#    active_manager = ActiveManager()
#    objects = models.Manager() # estas dos lineas me permiten marcar un objeto como cativo o inactivo pero la vaina es que practicamente elimina los objetos porque no os muestra por ningun lado, ni siquiera en el admin, la unica manera de regresarlos seria con el shell

    def __str__(self):
        return self.name
