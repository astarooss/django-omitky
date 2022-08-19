from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('fotogalerie', fotogalerie, name='fotogalerie'),
    path('cenik', cenik, name='cenik'),
    path('kontact', kontact, name='kontact'),
]


