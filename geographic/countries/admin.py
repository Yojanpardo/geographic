from django.contrib import admin
from .models import Country

# Register your models here.

@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display=('name','code','continent','classification',)
    list_filter=('classification',)
