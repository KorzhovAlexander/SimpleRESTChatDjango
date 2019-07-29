from django.contrib import admin
from django.urls import path
from UserRoom import views

urlpatterns = [
    path('', views.getRoom),
]
