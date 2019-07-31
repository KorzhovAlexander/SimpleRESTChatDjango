from django.contrib import admin
from django.urls import path
from UserRoom import views

urlpatterns = [
    path('', views.getAllRooms.as_view()),
    path('room-<int:pk>', views.getRoomById.as_view()),

    path('chat-<int:pk>/', views.getChatMessages.as_view()),
    path('send/', views.setChatMessage.as_view()),

]
