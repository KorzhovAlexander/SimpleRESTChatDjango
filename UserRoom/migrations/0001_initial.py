# Generated by Django 2.2.3 on 2019-07-30 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата присоединения пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='MessageChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=800, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки сообщения')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserRoom.ChatRoom', verbose_name='Комната чата')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='invited_user',
            field=models.ManyToManyField(related_name='invited_user', through='UserRoom.MessageChatRoom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель комнаты'),
        ),
    ]
