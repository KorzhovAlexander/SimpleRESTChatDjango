from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from UserRoom.models import ChatRoom, MessageChatRoom
from UserRoom.serializers import ChatRoomSerializer, MessageChatRoomSerializer, MessageCreateChatRoomSerializer


# Create your views here.

class getAllRooms(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()


class getRoomById(generics.RetrieveAPIView):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()


class getChatMessages(generics.ListAPIView):
    lookup_field = 'room'
    serializer_class = MessageChatRoomSerializer
    queryset = MessageChatRoom.objects.all()


class setChatMessage(generics.CreateAPIView):
    lookup_field = 'room'
    serializer_class = MessageCreateChatRoomSerializer
    queryset = MessageChatRoom.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,  room=self.kwargs['room'])
#
#
# class getChat(APIView):
#
#     def get(self, request):
#         room = request.GET.get('room')
#         chat = MessageChatRoom.objects.filter(room=room)
#         serializer = MessageChatRoomSerializer(chat, many=True)
#         return Response({"data": serializer.data})
#
#     def post(self, request):
#         dialog = MessageChatRoomSerializer(data=request.data)
#         if dialog.is_valid():
#             dialog.save(user=request.user)
#             return Response(status=200)
#         else:
#             return Response(status=400)
