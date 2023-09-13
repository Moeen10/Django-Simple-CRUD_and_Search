from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponse
# Create your views here.
def recepies(request):
    querySet = Receipe.objects.all();
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name =data.get('receipe_name')
        receipe_description =data.get('receipe_description')
       
        Receipe.objects.create(receipe_name = receipe_name ,
                           receipe_description=receipe_description , 
                           receipe_image = receipe_image )
        return redirect("/recepies/")
    
    
    if request.GET.get("search"):
        search_value = request.GET.get("search")
        querySet = querySet.filter(receipe_name__icontains =  search_value)
        print(search_value)

    
    context = {"recepies_object" : querySet,"page": "Add and Show recepies"}
    
    return render(request,"recepies.html",context)


def update_recepie(request,id):
    
    getObject = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        updateImage = request.FILES.get("receipe_image")
        updateName = data.get("receipe_name")
        updateDescription = data.get("receipe_description")

        getObject.receipe_name = updateName
        getObject.receipe_description = updateDescription
        if updateImage:
            getObject.receipe_image = updateImage
        
        getObject.save()
        return redirect("/recepies/")


    context = {"Object": getObject,"page": "Recepie Update"}
    return render(request,"update-recepies.html" , context)



def delete_recepie(request,id):
   
    #deleterRecepie = Receipe.objects.get(id = id)
    print("###")
    print(id)
    print("###")
    deleteQuery = Receipe.objects.get(id = id)
    print(deleteQuery.receipe_name)
    deleteQuery.delete()
  #  messages.success(request, 'Recipe deleted successfully')
    return redirect("/recepies/")