from django.shortcuts import render,HttpResponse
from .forms import *

# Create your views here.
def appointments(request):
    form = AppointmentForm(request.GET)
    print(form.data)
    return render(request, "appointments/index.html",{'app':form})

def register(request,name):
    return HttpResponse('salom brat')
