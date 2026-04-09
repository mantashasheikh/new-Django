from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
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
