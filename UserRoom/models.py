from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class ChatRoom(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Создатель комнаты',
        on_delete=models.CASCADE,
        related_name='user_create'
    )
    invited_user = models.ManyToManyField(
        User,
        verbose_name='Участники',
        related_name='invited_user'
    )
    date = models.DateTimeField(
        verbose_name='Дата присоединения пользователя',
        auto_now_add=True
    )

    def get_invited_user(self):
        return "\n".join([u.username for u in self.invited_user.all()])

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class MessageChatRoom(models.Model):
    room = models.ForeignKey(
        ChatRoom,
        verbose_name='Комната чата',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    message = models.TextField(
        verbose_name='Сообщение',
        max_length=800
    )
    date = models.DateTimeField(
        verbose_name='Дата отправки сообщения',
        auto_now_add=True
    )
