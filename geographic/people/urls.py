from django.urls import path
from .views import People

app_name = 'people'

urlpatterns=[
    path('',People.as_view(),name='home'),
]
