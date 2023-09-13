from django.shortcuts import render
from django.http import HttpResponse
from .templates import  *
def hello_world(request):
    return render(request,'index.html')

def home(request):
    context = {"page": "Home"}
    return render(request,'home.html',context)
def about(request):
    context = {"page": "About"}
    return render(request,'about.html',context)
def contact(request):


    
    context = {"page": "Contact"}
    return render(request,'contact.html',context)
