from django.conf import settings as global_settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from dentist.models import User as DentistUser
from .forms import *

# Create your views here.


def appointments(request):
    if request.user.username not in request.session:
        return redirect(f"{global_settings.LOGIN_URL}?next={request.path}")
    user = User.objects.get(username=request.user.username)
    dentist = DentistUser.objects.get(user=user)
    form = AppointmentForm(request.GET)
    return render(request, "appointments/index.html", {
        'app': form,
        'dentist': dentist
    })

def register(request,name):
    return HttpResponse('salom brat')
