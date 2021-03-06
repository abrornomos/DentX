from django.conf import settings as global_settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import get_language
from appointment.models import *
from dentist.models import User as DentistUser
from .handler import *

# Create your views here.


def board(request):
    if request.user.username not in request.session:
        return redirect(f"{global_settings.LOGIN_URL}?next={request.path}")
    user = User.objects.get(username=request.user.username)
    dentist = DentistUser.objects.get(user=user)
    queries = get_queries(Query.objects.filter(dentist=dentist))
    appointments = get_appointments(Appointment.objects.filter(dentist=dentist))
    return render(request, "baseapp/board.html", {
        'dentist': dentist,
        'queries': queries,
        'appointments': appointments,
    })
