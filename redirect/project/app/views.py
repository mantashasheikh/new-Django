from django.shortcuts import render , redirect
from django.http import JsonResponse
# Create your views here.
def demo(req):
    return redirect('home') #internal url....
    # return redirect('https://www.google.com') #external url....

def home(req):
    return render(req,'home.html')

# def demo1(req):
#     return redirect('index',1,'python')

# def index(req,x,y):
#     print(x,y)
#     return render(req,'index.html',{'a':x,'b':y})


def demo1(req):
    return redirect('index',a=1,b='python')

def index(req,a,b):
    print(a,b)
    return render(req,'index.html',{'a':a,'b':b})


# # Don't mix *args and **kwargs in call to reverse()!---------------
# def demo1(req):
#     return redirect('index',1,b='python') # Don't mix *args and **kwargs in call to reverse()!

# def index(req,a,b):
#     print(a,b)
#     return render(req,'index.html',{'a':a,'b':b}) 


def demo2(req):
    data = {'name':"Mantasha",
            'active1':True,
            'active2':False,
            'active3':None
            }
    return JsonResponse(data)
    
    # data = 10
    # return JsonResponse(data,safe=False)
    
    # data = 'Mantasha'
    # return JsonResponse(data,safe=False)
    
    # data = ['Mantasha']
    # return JsonResponse(data,safe=False)
    
    # data = ('Mantasha',)
    # return JsonResponse(data,safe=False)
    
    
    # error--------------------------------
    # # Object of type set is not JSON serializable(due to unordered collection)
    # data = {'Mantasha'}
    # return JsonResponse(data,safe=False)
    
    # # Object of type set is not JSON serializable(due to unordered collection)
    # data = frozenset({'Mantasha'})
    # return JsonResponse(data,safe=False)