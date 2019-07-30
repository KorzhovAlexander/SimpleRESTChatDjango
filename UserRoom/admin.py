from django.contrib import admin

from UserRoom.models import ChatRoom


# Register your models here.

class RoomAsAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("user", "get_invited_user", "date")


admin.site.register(ChatRoom, RoomAsAdmin)
