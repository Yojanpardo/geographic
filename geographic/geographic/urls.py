from django.contrib import admin
from django.urls import path
from continents.views import home, Continents, ContinentDetailView
from countries.views import Countries, CountryDetailView
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('class_home/', TemplateView.as_view(template_name='continents/home.html')),
    path('continents/',Continents.as_view()),
    path('continents/<int:code_id>', ContinentDetailView.as_view()),
    path('countries/',Countries.as_view()),
    path('countries/<code>/',CountryDetailView.as_view()),
]
