from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='home'),
  path('doctors/',views.doctors,name="doctor"),
  path('bookPage/',views.bookPage,name='booking'),
  path('contact/',views.contact,name="contact"),
  path('department/',views.department,name="department"),
  path('about/',views.about,name="about")
]

