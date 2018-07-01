from django.contrib import admin
from django.urls import path, include
from continents.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('continents/',include('continents.urls',namespace='continents')),
    path('countries/',include('countries.urls',namespace='countries')),
    path('people/',include('people.urls',namespace='people')),
    path('capitals/',include('capitals.urls',namespace='capitals')),
]
