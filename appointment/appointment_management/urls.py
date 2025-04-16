from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('view_appointments', views.view_appointments, name='view_appointments'),
    path('complete_appointment', views.complete_appointment, name='complete_appointment'),
]