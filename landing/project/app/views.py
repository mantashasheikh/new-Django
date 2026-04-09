from django.shortcuts import render
from django.urls import render

# Create your views here.
def home(req):
    return render(req , 'home.html')

def landing(req):
    return render(req , 'landing.html')
