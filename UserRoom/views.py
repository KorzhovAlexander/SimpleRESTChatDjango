from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from UserRoom.models import ChatRoom, MessageChatRoom
from UserRoom.serializers import ChatRoomSerializer, MessageChatRoomSerializer


# Create your views here.


class getRoom(APIView):

    def get(self, request):
        room = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(room, many=True)
        return Response({"data": serializer.data})


class getChat(APIView):

    def get(self, request):
        room = request.GET.get('room')
        chat = MessageChatRoom.objects.filter(room=room)
        serializer = MessageChatRoomSerializer(chat, many=True)
        return Response({"data": serializer.data})
