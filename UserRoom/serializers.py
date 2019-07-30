from rest_framework.serializers import ModelSerializer

from UserRoom.models import ChatRoom
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'username')

