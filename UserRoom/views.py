from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from UserRoom.models import ChatRoom
from UserRoom.serializers import ChatRoomSerializer


# Create your views here.


class getRoom(APIView):

    def get(self, request):
        room = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(room, many=True)
        return Response({"data": serializer.data})
