from django.shortcuts import render
from rest_framework import generics

from User.serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class getAllUsers(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
