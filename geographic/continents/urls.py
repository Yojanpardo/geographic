from django.urls import path
from django.views.generic import TemplateView
from .views import Continents, ContinentDetailView

app_name = 'continents'

urlpatterns = [
    path('class_home/', TemplateView.as_view(template_name='continents/home.html'),name='class_home'),
    path('',Continents.as_view(), name='home'),
    path('<int:id>/', ContinentDetailView.as_view(),name='continent_detail'),
]
