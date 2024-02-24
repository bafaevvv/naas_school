from django.shortcuts import render
from .models import *

def home(request):
    home_page = Teacher.objects.all()
    return render(request, 'base.html', {'home': home_page})

def course(request):
    course = Course.objects.all()
    return render(request, 'base.html', {'course': course})