from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from .forms import *

# Create your views here.


def signin(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(
                request,
                username=loginform.cleaned_data['username'],
                password=loginform.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                request.session[user.get_username()] = user.get_username()
                return redirect("appointment:appointments")
            else:
                return render(request, "login/login.html", {
                    'loginform': loginform,
                    'error_message': _("Noto'g'ri login yoki parol")
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


def signout(request):
    if request.user.username in request.session:
        del request.session[request.user.username]
    logout(request)
    return redirect("login:signin")


def dashboard(request):
    return render(request, "dentist/dashboard.html", {
        'user': request.user
    })
