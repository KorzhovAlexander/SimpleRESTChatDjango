from django.contrib import admin
from django.urls import path, include

from User import views

urlpatterns = [
    path('', views.getAllUsers.as_view()),
    path('<int:pk>', views.getUserById.as_view()),
]
