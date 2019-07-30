from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class ChatRoom(models.Model):
    user = models.ForeignKey(User, verbose_name='Создатель комнаты', on_delete=models.CASCADE)
    invited_user = models.ManyToManyField(User, through='MessageChatRoom', related_name='invited_user')
    date = models.DateTimeField(verbose_name='Дата присоединения пользователя', auto_now_add=True)


class MessageChatRoom(models.Model):
    room = models.ForeignKey(ChatRoom, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Сообщение', max_length=800)
    date = models.DateTimeField(verbose_name='Дата отправки сообщения', auto_now_add=True)
