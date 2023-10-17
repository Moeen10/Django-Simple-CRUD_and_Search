from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shed.forms import ShedForm
from .models import Shed_registration
from django.contrib import messages

@login_required(login_url='/login/')
def shed_registration(request):
    form = ShedForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            shed = form.save(commit=False)
            shed.owner = request.user  
            shed.save()
            messages.info(request, "Shed Create Successfully") 
            print("Shed saved successfully")
            return redirect('shed_registration')
            
        else:
            print("Form is not valid")
    else:
        form = ShedForm()  

    return render(request, "shed_registration.html", {'form': form})
