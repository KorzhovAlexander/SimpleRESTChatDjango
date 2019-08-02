from django.contrib import admin
from django.urls import path
from UserRoom import views

urlpatterns = [
    path('', views.getAllRooms.as_view()),
    # path('room-<int:pk>', views.getRoomById.as_view()),

    path('room-<int:room>/', views.getChatMessages.as_view()),
    path('room-<int:room>/send/', views.setChatMessage.as_view()),

]
