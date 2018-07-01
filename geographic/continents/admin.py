from django.contrib import admin
from .models import Continent
# Register your models here.

@admin.register(Continent)
class AdminContinent(admin.ModelAdmin):
    list_display=('name','color','population',)
