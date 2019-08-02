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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MessageChatRoom
        fields = '__all__'


class MessageCreateChatRoomSerializer(ModelSerializer):
    room = ChatRoomSerializer(many=True, read_only=True, source='invited_user')

    class Meta:
        model = MessageChatRoom
        fields = ('message', 'room')
