from django.urls import path
from . import views


urlpatterns = [
    path('', views.appointments, name='appointments'),
    path('table/', views.table, name='table'),
]

