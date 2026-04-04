print("From views.py............")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingpage(req):
    
    return HttpResponse("This is the landing page")