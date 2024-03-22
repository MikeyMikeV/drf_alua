from django.contrib import admin
from django.urls import path, include
from music.views import MusicViewSet, MusicUploadViewSet
from accounts.serializers import  UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('music',MusicViewSet)
router.register('upload_music',MusicUploadViewSet, basename='music_upload')

urlpatterns = [
    path('',include('music.urls')),
    path('rest/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('accounts/',include('accounts.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)