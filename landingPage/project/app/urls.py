# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.landingpage,name='landingpage'),   
# ]

print("From app/urls.py............")
from django.urls import path
from .views import *

urlpatterns = [
    path('',landingpage,name='landingpage'),   
]