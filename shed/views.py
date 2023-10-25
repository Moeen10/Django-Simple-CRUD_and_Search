from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shed.forms import ShedForm
from .models import Shed_registration , FormData
from django.contrib import messages
from .serializers import ShedRegistrationSerializer , FormDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


@login_required(login_url='/login/')
@api_view(['POST'])
def shed_registration(request):
    form = ShedForm(request.POST or None)
    
    if request.method == 'POST':
        serializer = ShedRegistrationSerializer(data=request.data)
        if form.is_valid():
            shed = form.save(commit=False)
            shed.owner = request.user  
            shed.save()
            messages.info(request, "Shed Create Successfully") 
            print("Shed saved successfully")
            serializer = ShedRegistrationSerializer(shed)  # Serialize the saved object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect('shed_registration')
                
        else:
            print("Form is not valid")
    else:
        form = ShedForm()  

    return render(request, "shed_registration.html", {'form': form})



@api_view(['GET'])
def list_sheds(request):
    sheds = Shed_registration.objects.all()
    serializer = ShedRegistrationSerializer(sheds, many=True)
    return Response(serializer.data)






class FormDataView(APIView):
    def post(self, request):
        serializer = FormDataSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print( serializer.validated_data)
            print( serializer.validated_data.get('name'))

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)