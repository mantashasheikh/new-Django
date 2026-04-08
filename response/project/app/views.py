from django.shortcuts import render

# Create your views here.
def demo(req):
    # response = render(req,'demo.html')
    # response = render(req,'demo.html',{'name':'mantasha', 'city':'Bhopal'} )
    # return response
    
    data = {'name': 'Rimsha', 'age': 20}
    # return render(req,'demo.html', data)
    
    return render(req,'demo.html',{'x': data})
    
    
