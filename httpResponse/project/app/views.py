from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def demo(req):
    # data = 10
    # data = "python"
    # data = "<h1>python</h1>"
    # return HttpResponse(data , content_type="text/html")
    data = {'name':'mantasha'}
    
    return HttpResponse(json.dumps(data) , content_type="application/json")

