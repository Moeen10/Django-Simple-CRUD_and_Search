from decimal import Decimal
from django.shortcuts import render, redirect
from .models import *
from .forms import CowRegistrationForm
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseRedirect,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

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



class CowRegistrationView(APIView):
    def post(self, request, format=None):
        print(request.data)
        allDesease = request.data.get('desease') 
        print(allDesease)
        serializer = CowRegistrationSerializer(data=request.data)
        age  = request.data.get('age')
        age = int(age)
        print("88888888888888888888888888888")
        
        # purchase date purchase_date_value

        purchase_date_value = request.data.get('purchase_date')
        # whereas in model the purchase_date support date value like 2000-10-20(YYYY-MM-DD) so total leth of the data is 10 thats why i set condition 10==purchase value 
        if len(purchase_date_value) != 10:
            request.data['purchase_date'] = None
            purchase_date_value = request.data.get('purchase_date')
            print(purchase_date_value)

        if serializer.is_valid():
            print("VALID")

            # Handle Dease 
            allDesease = request.data.get('desease') 
            print(allDesease)

            # Handle Medicine
            allMedicine = request.data.get('medicine') 
            print(allMedicine)
           
            # Handle Vaccine
            allVaccine = request.data.get('vaccine') 
            print(allVaccine)
            
            
           

            cow_registration = CowRegistration(
                cattle_id=request.data.get('cattle_id'),
                purchase_date=purchase_date_value,
                
                age=request.data.get('age'),
                color=request.data.get('color'),
                date_of_birth = request.data.get('date_of_birth'),
                breeding_rate = int(request.data.get('breeding_rate')),
                weight = Decimal(request.data.get('weight')),
                milk_yield = Decimal(request.data.get('milk_yield')),
                active = True,
                origin = request.data.get('origin'),
                gender = request.data.get('gender'),
                helth_status = request.data.get('helth_status'),
                provable_heat_date = request.data.get('provable_heat_date'),
                heat_status = request.data.get('heat_status'),
                actual_heat_date = request.data.get('actual_heat_date'),
                semen_push_status = request.data.get('semen_push_status'),
                pregnant_date = request.data.get('pregnant_date'),
                delivery_status = request.data.get('delivery_status'),
                delivery_date = request.data.get('delivery_date'),
                # Add more fields as needed
            )
            # Save the instance to the database

            cow_registration.save()
            print("KIRRRRRRRRRRRR")
            cow_registration.desease.set(allDesease)
            cow_registration.medicine.set(allMedicine)
            cow_registration.vaccine.set(allVaccine)
            print("SAVE HOISE")

            if request.data.get('helth_status') == "Sick":
                cow_id = request.data.get('helth_status')
                sickCow = Sick_Cow(
                    cow_id=cow_registration,
                ) 
                sickCow.save();
                sickCow.cow_desease.set(allDesease)
                print("Cow Sick Also done Complete")


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# def allCow(request):
#     allCowList = CowRegistration.objects.all() 
#     serializer = AllCowSerializer(allCowList, many = True)

#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')


class MasterDeseaseList(APIView):
    def get(self, request):
        deseases = MasterDesease.objects.all()
        print("de", deseases)
        serializer = MasterDeseaseSerializer(deseases, many=True)
        print("ssde", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MasterDeseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class MasterVaccineList(APIView):
    def get(self, request):
        vaccines = MasterVaccine.objects.all()
        print("de", vaccines)
        serializer = MasterVaccineSerializer(vaccines, many=True)
        print("ssde", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = MasterDeseaseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterMedicineList(APIView):
    def get(self, request):
        medicine = MasterMedicin.objects.all()
        print("de", medicine)
        serializer = MasterMedicinSerializer(medicine, many=True)
        print("ssde", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
 


class CowProfile(APIView):
    def get(self, request):
        try:
            cows = CowRegistration.objects.all()
            serializer = CowRegistrationSerializer(cows, many=True)
        except ObjectDoesNotExist:
        # Handle the exception here, and set a specific error message
            error_message = "The object does not exist."
            return HttpResponse(error_message, status=404)  # 404 Not Found
        except Exception as e:
        # Handle other exceptions as needed, and set appropriate status code and message
            error_message = "An error occurred: " + str(e)
            return HttpResponse(error_message, status=500) 
        
            
        return Response(serializer.data, status=status.HTTP_200_OK)
        

