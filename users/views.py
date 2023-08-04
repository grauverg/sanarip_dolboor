from rest_framework import generics

from . import models
from . import serializers
from . import permissions
from products.permissions import IsAuthor


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsNotAuthenticatedOrReadOnly]


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthor, ]
