from django.urls import path
from .views import Countries, CountryDetailView

app_name = 'countries'

urlpatterns =[
    path('',Countries.as_view(),name='home'),
    path('<code>/',CountryDetailView.as_view(),name='country_detail'),
]
