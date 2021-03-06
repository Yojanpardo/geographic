from django.contrib import admin
from .models import Person
# Register your models here.

@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display=('name','last_name','phone_number','is_active',)
    list_filter=('is_active',)
