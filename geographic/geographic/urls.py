from django.contrib import admin
from django.urls import path
from continents.views import home, continents
from countries.views import countries
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('continents/',continents),
    path('countries/',countries),
]
