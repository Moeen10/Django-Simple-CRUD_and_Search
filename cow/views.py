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
from datetime import datetime

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



# FOR MOBILE

#COW Registration / POST

class CowRegistrationView(APIView):
    def post(self, request, format=None):
        print(request.data)
        allDesease = request.data.get('desease') 
        print(allDesease)
        try:
            serializer = CowRegistrationSerializer(data=request.data)
            age  = request.data.get('age')
            age = int(age)
        except:
            return Response({"message": f"Insert Valid Data"}, status=status.HTTP_400_BAD_REQUEST)
        print("88888888888888888888888888888")
        
        # purchase date purchase_date_value

        purchase_date_value = request.data.get('purchase_date')
        # whereas in model the purchase_date support date value like 2000-10-20(YYYY-MM-DD) so total leth of the data is 10 thats why i set condition 10==purchase value 
        
        current_date = datetime.now().strftime("%Y-%m-%d")
        request.data['purchase_date'] = current_date
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
    
       
            try:
                print("1........555555555555555555555555555555555")
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
            except:
                print("2........555555555555555555555555555555555")
                return Response({"message": f"Object Create Failed"},status=status.HTTP_400_BAD_REQUEST)
            print("3........555555555555555555555555555555555")
            if request.data.get('helth_status') == "Sick":
                cow_id = request.data.get('helth_status')
                sickCow = Sick_Cow(
                    cow_id=cow_registration,
                ) 
                sickCow.save();
                sickCow.cow_desease.set(allDesease)
                print("Cow Sick Also done Complete")


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": f"Registration Failed"}, status=status.HTTP_400_BAD_REQUEST)

#COW Profile Page Show / GET

class CowProfile(APIView):
    def get(self, request):
        try:
            cows = CowRegistration.objects.all()
            serializer = CowShowSerializer(cows, many=True)
          




        except ObjectDoesNotExist:
        # Handle the exception here, and set a specific error message
            error_message = "The object does not exist."
            return HttpResponse(error_message, status=404)  # 404 Not Found
        except Exception as e:
        # Handle other exceptions as needed, and set appropriate status code and message
            error_message = "An error occurred: " + str(e)
            return HttpResponse(error_message, status=500) 
        
            
        return Response(serializer.data, status=status.HTTP_200_OK)
  
#COW Profile Update / PUT

class CowUpdate(APIView):
    def put(self, request):
        cow_id =request.data.get('id')

        
        
    # Disease Id found from name
        deseaseList = request.data['desease']
        print("^^^^^^^^^^^^^^^^^^^^^^")
        print(deseaseList)
        disease_ids = []
        for disease_name in deseaseList:
            try:
                disease = MasterDesease.objects.get(desease_name=disease_name)
                disease_ids.append(disease.id)
            except MasterDesease.DoesNotExist:
                pass

    # Medicine Id found from name
        medicineList = request.data['medicine']
        medicine_ids = []
        for medicine_name in medicineList:
            try:
                medicine = MasterMedicin.objects.get(medicine_name=medicine_name)
                medicine_ids.append(medicine.id)
            except MasterMedicin.DoesNotExist:
                pass

    # VACCIne Id found from name
        vaccineList = request.data['vaccine']
        vaccine_ids = []
        for vaccine_name in vaccineList:
            try:
                vaccine = MasterVaccine.objects.get(vaccine_name=vaccine_name)
                vaccine_ids.append(vaccine.id)
            except MasterVaccine.DoesNotExist:
                pass
        
        
        request.data['vaccine'] = vaccine_ids
        request.data['medicine'] = medicine_ids
        request.data['desease'] = disease_ids
        data= request.data
        try:
            cow = CowRegistration.objects.get(id=cow_id)
        except CowRegistration.DoesNotExist:
            return Response({"message": "Cow not found"}, status=status.HTTP_404_NOT_FOUND)
        if request.data['helth_status']=="Good":
                request.data['vaccine'] = []
                request.data['medicine'] = []
                request.data['desease'] = []

        serializer = CowRegistrationSerializer(cow, data=data, partial=True)  # Use the serializer with the existing instance (cow)
        if serializer.is_valid():
            print("OK OK OK OK OK")
            serializer.save()
            return Response({"message": f"Update Sucessfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": f"Update Failed"}, status=status.HTTP_400_BAD_REQUEST)
        
class MilkPost(APIView):
 
 def post(self, request, format=None):
        try:
            serializer = MilkYieldSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Post Successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Insert Valid Data"}, status=status.HTTP_400_BAD_REQUEST)
 
 def get(self, request):
        allCowsMilkYield = MilkYield.objects.all()
        print("de", allCowsMilkYield)
        serializer = MilkYieldSerializer(allCowsMilkYield, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
 

      