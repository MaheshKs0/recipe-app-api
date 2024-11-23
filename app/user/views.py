from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer



class CreateTokenView(ObtainAuthToken):
    """Create a new auth token view"""
    serializer_class = AuthTokenSerializer
    renderer_Classes = api_settings.DEFAULT_RENDERER_CLASSES


