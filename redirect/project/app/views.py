from django.shortcuts import render , redirect

# Create your views here.
def demo(req):
    return redirect('home') #internal url....
    # return redirect('https://www.google.com') #external url....

def home(req):
    return render(req,'home.html')
