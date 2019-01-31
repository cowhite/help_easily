from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import PostContentSerializer


class PostContentCreateView(generics.CreateAPIView):
    serializer_class = PostContentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
