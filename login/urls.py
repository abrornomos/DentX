from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
