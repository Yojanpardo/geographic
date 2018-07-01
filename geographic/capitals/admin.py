from django.contrib import admin
from .models import Capital
# Register your models here.

@admin.register(Capital)
class AdminCapital(admin.ModelAdmin):
    list_display=('name','country')
