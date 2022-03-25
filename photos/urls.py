from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('current/',views.photos_of_day,name = 'photosToday')
]