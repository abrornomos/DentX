from django.urls import path
from . import views


urlpatterns = [
    path('', views.appointments, name='appointments'),
    path('<str:name>/', views.register, name='register'),
]

