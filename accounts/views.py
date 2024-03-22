from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView 

from .serializers import LoginUserSerializer
from django.contrib.auth import login

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    
# class CustomLoginView(RestLoginView):
#     permission_classes =[AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = LoginUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data('user')
#         login(request, user)
#         return super().post(request, format = None)
    