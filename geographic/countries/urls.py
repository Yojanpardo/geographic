from django.urls import path
from .views import Countries, CountryDetailView, SearchCountry

app_name = 'countries'

urlpatterns =[
    path('',Countries.as_view(),name='home'),
    path('search/<query>/',SearchCountry.as_view(), name='search'),
    path('<code>/',CountryDetailView.as_view(),name='country_detail'),
]
