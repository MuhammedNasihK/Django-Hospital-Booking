from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctors
from .forms import Bookingform

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = Bookingform(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            
    form = Bookingform()

    form_details = {
        'form' : form
    }
    return render(request,'booking.html',form_details)

def doctors(request):
    doc_detail = {
        'doctors' : Doctors.objects.all()
    }
    return render(request,'doctors.html',doc_detail)

def contact(request):
    return render(request,'contact.html')

def department(request):
    department = {
        'dept' : Department.objects.all()
    }

    return render(request,'department.html',department)

   