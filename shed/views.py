from django.shortcuts import render
from .models import Shed_registration

# Create your views here.


def shed_registration(request):
    context = "hello"
    if request.method == "POST":
        data = request.POST
        shed_name =  data.get('shed_name')
        shed_length =  data.get('shed_length')
        shed_width =  data.get('shed_width')
        cowNumber =  data.get('cowNumber')
        email =  data.get('email')
        phoneNumber =  data.get('phoneNumber')
        shed_location =  data.get('shed_location')
       
        Shed_registration.objects.create(
            shedName =  shed_name,
            shedLength= shed_length , 
            shedWidth = shed_width,
            shedLocation = shed_location,
            phoneNumber = phoneNumber,
            email = email,
            number_of_cow = cowNumber,
           )
        
        

    return render(request,"shed_registration.html",{'context' : context})