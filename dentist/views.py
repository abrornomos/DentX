from django.shortcuts import render
from .models import *


def dentist(request):
    return render(request,'dentist/dashboard.html')

