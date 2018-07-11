from django.urls import path
from django.views.generic import TemplateView
from .views import Continents, ContinentDetailView, register_continent

app_name = 'continents'

urlpatterns = [
    path('class_home/', TemplateView.as_view(template_name='continents/home.html'),name='class_home'),
    path('',Continents.as_view(), name='home'),
    path('<int:pk>/', ContinentDetailView.as_view(),name='continent_detail'),
    path('register_continent/', register_continent,name='register_continent'),
]
