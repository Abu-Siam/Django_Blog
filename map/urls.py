from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home,name='map-home'),
    path('', views.get_path,name='map-home'),
    path('about/',views.about,name='map-about'),
    path('map/',views.map,name='map-design')
]