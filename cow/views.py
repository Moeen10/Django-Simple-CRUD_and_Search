from django.shortcuts import render, redirect
from .models import CowRegistration, Sick_Cow
from .forms import CowRegistrationForm
from .serializers import AllCowSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseRedirect,HttpResponse


def cow_registration(request):
    if request.method == 'POST':
        form = CowRegistrationForm(request.POST)
        if form.is_valid():
            cow = form.save()
            if cow.helth_status  == 'Sick':
                print(cow)
                print(cow.desease)
                Sick_Cow.objects.create(cow_id=cow, cow_desease=cow.desease)
            return redirect('recepies') 
    else:
        form = CowRegistrationForm()
    
    context = {'form': form}
    return render(request, 'addCow.html', context)

def allCow(request):
    allCowList = CowRegistration.objects.all() 
    serializer = AllCowSerializer(allCowList, many = True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')