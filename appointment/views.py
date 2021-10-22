from django.conf import settings as global_settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils.translation import get_language
from baseapp.models import Language
from dentist.models import User as DentistUser, User_translation as DentistUserTranslation, Service, Service_translation
from datetime import datetime, date, timedelta
from .forms import *
from .handler import *
from .models import *
from .var import *

# Create your views here.


def appointments(request):
    if request.user.username not in request.session:
        return redirect(f"{global_settings.LOGIN_URL}?next={request.path}")
    if request.method == "POST":
        print(request.POST)
    user = User.objects.get(username=request.user.username)
    dentist = DentistUser.objects.get(user=user)
    dentist_translation = DentistUserTranslation.objects.filter(
        dentist=dentist,
        language__name=Language.objects.get(pk=dentist.language_id)
    )[0]
    services = get_services(
        Service.objects.filter(dentist=dentist),
        dentist.language_id
    )
    appointmentform = AppointmentForm()
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return render(request, "appointments/index.html", {
        'appointmentform': appointmentform,
        'dentist': dentist,
        'dentist_translation': dentist_translation,
        'services': services
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
    else:
        temp = date.today()
        day = temp - timedelta(days=temp.weekday())
    days = [day]
    html = f"<table class=\"time-table table-bordered text-center\"><thead><tr class=\"text-center\"><th>Time</th><th>{day.day}-{MONTHS[day.month - 1].lower()}<br>{DAYS[day.weekday()]}</th>"
    for i in range(6):
        temp = days[len(days) - 1] + timedelta(days=1)
        days.append(temp)
        html += f"<th>{temp.day}-{MONTHS[temp.month - 1].lower()}<br>{DAYS[temp.weekday()]}</th>"
    html += "</tr></thead><tbody>"
    user = User.objects.get(username=request.user.username)
    dentist = DentistUser.objects.get(user=user)
    day_begin = datetime(
        days[0].year,
        days[0].month,
        days[0].day,
        dentist.worktime_begin.hour,
        dentist.worktime_begin.minute
    )
    day_end = datetime(
        days[0].year,
        days[0].month,
        days[0].day,
        dentist.worktime_end.hour,
        dentist.worktime_end.minute
    )
    while day_begin <= day_end:
        html += f"<tr><th>{day_begin.strftime('%H:%M')}</th>"
        for day in days:
            if compare_time(day_begin, Appointment.objects.filter(
                begin__year=day_begin.year,
                begin__month=day_begin.month,
                begin__day=day_begin.day
            )):
                html += f"<td>{day_begin.strftime('%H:%M')}</td>"
        day_begin += timedelta(minutes=15)
        html += "</tr>"
    html += "</tbody></table>"
    return HttpResponse(html)
