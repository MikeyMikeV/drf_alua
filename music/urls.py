from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('upload/', views.music_upload, name='music_upload'),
    path('list', views.music_list, name='music_list'),
]