from django.shortcuts import render
from django.http import HttpResponse
from .models import Department

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    department = {
        'dept' : Department.objects.all()
    }

    return render(request,'department.html',department)