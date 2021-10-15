from django.conf import settings as global_settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from dentist.models import User as DentistUser
from datetime import date, timedelta
from .forms import *

# Create your views here.


def appointments(request):
    if request.user.username not in request.session:
        return redirect(f"{global_settings.LOGIN_URL}?next={request.path}")
    user = User.objects.get(username=request.user.username)
    dentist = DentistUser.objects.get(user=user)
    form = AppointmentForm(request.GET)
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return render(request, "appointments/index.html", {
        'app': form,
        'dentist': dentist,
        'monday': monday
    })

def table(request):
    if request.method == "POST":
        if request.POST['direction'] == "left":
            day = date(
                int(request.POST['year']),
                int(request.POST['month']),
                int(request.POST['day'])
            ) - timedelta(weeks=1)
        elif request.POST['direction'] == "right":
            temp = date(
                int(request.POST['year']),
                int(request.POST['month']),
                int(request.POST['day'])
            )
            day = temp + timedelta(days=temp.weekday(), weeks=1)
        html = f"<h1>{day}</h1>"
        return HttpResponse(html)
    else:
        temp = date.today()
        html = f"<h1>{temp - timedelta(days=temp.weekday())}</h1>"
        return HttpResponse(html)
