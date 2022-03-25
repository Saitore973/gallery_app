from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('current/',views.photos_of_day,name = 'photosToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
    ] 
