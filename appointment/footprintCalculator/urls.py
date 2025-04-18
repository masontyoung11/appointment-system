from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('carbon_quiz', views.carbon_quiz, name='carbon_quiz'),
]