from django.contrib.auth.models import User
from rest_framework import serializers,viewsets
from django.contrib.auth import authenticate

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get['username']
        password = attrs.get['password']

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get['request'], username = username, password=password)
            else:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)
            
            if not user:
                msg = {'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return super().validate(attrs)