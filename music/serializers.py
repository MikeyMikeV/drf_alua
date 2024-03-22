from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Music
from drf_extra_fields.fields import Base64ImageField

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    cover = Base64ImageField(required = False)
    class Meta:
        model = Music
        fields = '__all__'

class MusicFileAddSerialiser(serializers.Serializer):
    music_id = serializers.IntegerField()
    file = serializers.FileField()
    class Meta:
        fields = ('id','file',)