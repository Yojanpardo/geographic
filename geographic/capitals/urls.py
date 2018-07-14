from django.urls import path
from .views import Capitals, register_capital

app_name = 'capitals'

urlpatterns = [
    path('',Capitals.as_view(),name='home'),
    path('register_capital/',register_capital,name='register_capital'),
]
