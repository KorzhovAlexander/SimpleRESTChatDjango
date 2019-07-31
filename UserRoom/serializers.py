from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from UserRoom.models import ChatRoom, MessageChatRoom
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ChatRoomSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    invited_user = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'


class MessageChatRoomSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MessageChatRoom
        fields = '__all__'
