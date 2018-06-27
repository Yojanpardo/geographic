from django.contrib import admin
from django.urls import path
from continents.views import home, Continents, ContinentDetailView
from countries.views import Countries, CountryDetailView
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('class_home/', TemplateView.as_view(template_name='continents/home.html'),name='class_home'),
    path('continents/',Continents.as_view(), name='continents'),
    path('continents/<int:code_id>', ContinentDetailView.as_view(),name='continent_detail'),
    path('countries/',Countries.as_view(),name='countries'),
    path('countries/<code>/',CountryDetailView.as_view(),name='country_detail'),
]
