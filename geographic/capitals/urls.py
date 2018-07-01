from django.urls import path
from .views import Capitals

app_name = 'capitals'

urlpatterns = [
    path('',Capitals.as_view(),name='home'),
]
