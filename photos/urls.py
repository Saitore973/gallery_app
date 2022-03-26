from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('current/',views.photos_of_day,name = 'photosToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
    path('search/', views.search_results, name='search_results')
    ] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
