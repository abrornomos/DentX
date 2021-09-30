from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .forms import *

# Create your views here.


def signin(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                login(request, user)
                return redirect("login:dashboard")
            else:
                return render(request, "login/login.html", {
                    'loginform': loginform,
                    'error_message': _("Неверный логин и пароль")
                })
        else:
            loginform = LoginForm()
            return render(request, "login/login.html", {
                'loginform': loginform,
                'error_message': None
            })
    else:
        loginform = LoginForm()
        return render(request, "login/login.html", {
            'loginform': loginform,
            'error_message': None
        })


def signup(request):
    return render(request, "login/signup.html")


def signout(request):
    logout(request)
    return redirect("login:signin")


def dashboard(request):
    return render(request, "dentist/dashboard.html", {
        'user': request.user
    })
