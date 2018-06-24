from django.contrib import admin
from django.urls import path
from continents.views import home, Continents
from countries.views import Countries
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('class_home/', TemplateView.as_view(template_name='continents/home.html')),
    path('continents/',Continents.as_view()),
    path('countries/',Countries.as_view()),
]
