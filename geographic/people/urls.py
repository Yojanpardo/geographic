from django.urls import path
from .views import People, register_person

app_name = 'people'

urlpatterns=[
    path('',People.as_view(),name='home'),
    path('register_person',register_person,name='register_person'),
]
