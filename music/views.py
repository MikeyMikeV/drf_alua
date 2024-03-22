from django.shortcuts import render
from rest_framework.decorators import api_view

from music.models import Music
from .serializers import MusicSerializer, MusicFileAddSerialiser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response


def home_page(request):
    return render(request, 'base.html',{})

def music_list(request):
    return render(request, 'music_list.html',{})

def music_upload(request):
    return render(request, 'music_upload.html',{})

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser,)


class MusicUploadViewSet(viewsets.ViewSet):
    serializer_class = MusicFileAddSerialiser
    parser_classes = (JSONParser, MultiPartParser)
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        return Response('Upload')
    
    def create(self, request):
        music_id = request.POST.get('music_id')
        file = request.FILES.get('file_field')
        music = Music.objects.get(pk = music_id)
        music.file = file
        music.save()
        return Response('File Uploaded')