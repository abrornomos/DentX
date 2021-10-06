from django.urls import path
from . import views

urlpatterns = [
    path('dentist/',views.dentist,name='dentist')
]
