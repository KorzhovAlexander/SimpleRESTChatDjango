from django.contrib import admin
from django.urls import path
from UserRoom import views

urlpatterns = [
    path('', views.getRoom.as_view()),
    path('chat/', views.getChat.as_view()),
]
