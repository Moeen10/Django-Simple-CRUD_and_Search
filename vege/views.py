from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required(login_url='/login/')
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

def loginPage(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        print("6666666666666666666666")
        print(username)
        print(password)
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Wrong Username")
            return redirect('/login/')
        else:        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('/recepies/')
            else:
                messages.error(request,"Your password or username is not Correct")

    context = {
        'page': "Login"
    }
    return render(request,"login.html",context)


def registration(request):
    if request.method == "POST":
        data = request.POST
        FName = data.get("first_name")
        LName = data.get("last_name")
        username = data.get("username")
        password = data.get("password")



        existuser = User.objects.filter(username=username)
        print("+++++++++++++++++++++++++")
        print(existuser.exists())
        if existuser.exists():
            messages.info(request, "Change user name because this user name is already taken")    
            return redirect('/register/')
        
        user = User.objects.create(
            username = username,
            first_name = FName,
            last_name = LName,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully") 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('/recepies/')

    context = {
        'page': "Registration"
    }
    return render(request, "registration.html", context)

def logout_page(request):
    logout(request)
    return redirect('/login/')