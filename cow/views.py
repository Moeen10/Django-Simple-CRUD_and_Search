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


# class MasterMedicineList(APIView):
#     def get(self, request):
#         medicine = MasterMedicin.objects.all()
#         print("de", medicine)
#         serializer = MasterVaccineSerializer(medicine, many=True)
#         print("ssde", serializer.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

class MasterMedicineList(APIView):
    def get(self, request):
        medicine = MasterMedicin.objects.all()
        print("de", medicine)
        serializer = MasterMedicinSerializer(medicine, many=True)
        print("ssde", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
 

# class CowRegistrationView(APIView):
#     def post(self, request, format=None):
#         print(request.data)
#         serializer = CowRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowRegistrationView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = CowRegistrationSerializer(data=request.data)
        age  = request.data.get('age')
        age = int(age)
        print("88888888888888888888888888888")
        print(type(age))
        if serializer.is_valid():
            print("VALID");

            # Handle Dease 
            allDesease_names = request.data.get('desease') 
            postDesease = [MasterDesease.objects.get(desease_name=desease_name) for desease_name in allDesease_names]
            print("Dease : + ",postDesease)

            # Handle Medicine
            allMedicine_names = request.data.get('medicine') 
            postMedicine = [MasterMedicin.objects.get(medicine_name=medicine_name) for medicine_name in allMedicine_names]
            print("Medicine : + ",postMedicine)

            # Handle Vaccine
            allVaccine_names = request.data.get('vaccine') 
            postVaccine = [MasterVaccine.objects.get(vaccine_name=vaccine_name) for vaccine_name in allVaccine_names]
            print("Vaccine : + ",postVaccine)

            cow_registration = CowRegistration(
                cattle_id=request.data.get('cattle_id'),
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
            cow_registration.desease.set(postDesease)
            cow_registration.medicine.set(postMedicine)
            cow_registration.vaccine.set(postVaccine)
            print("SAVE HOISE")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)