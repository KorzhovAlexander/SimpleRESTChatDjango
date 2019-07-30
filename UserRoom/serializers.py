from rest_framework.serializers import ModelSerializer

from UserRoom.models import ChatRoom
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ChatRoomSerializer(ModelSerializer):
    user = UserSerializer()
    invited_user = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = '__all__'
