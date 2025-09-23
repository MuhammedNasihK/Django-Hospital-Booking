from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page(request):

    numbers = {
        'name' : 'nasih',
        'num': [1,2,3,4,5,6,7,8],
    }

    return render(request,'home.html',numbers)

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')