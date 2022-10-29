import imp
from django.shortcuts import render
from django.http import HttpResponse
from polls.forms import BookingForm
from .models import Department,Doctors
# Create your views here.

def index(request):
  return render(request,'index.html')

def bookPage(request):
  #post method to save data to database
  if request.method == "POST":
    form = BookingForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'confirmation.html')
  #get method to display form
  form = BookingForm()
  dict_form = {
    'form' : form
  }
  return render(request,'bookPage.html',dict_form)

def doctors(request):
  dict_docs={
    'doctors':Doctors.objects.all()
  }
  return render(request,'doctors.html',dict_docs)

def contact(request):
  return render(request,'contacts.html')

def department(request):
  dict_dept={
    'dept':Department.objects.all()
  }
  return render(request,'department.html',dict_dept)

def about(request):
  return render(request,'about.html')