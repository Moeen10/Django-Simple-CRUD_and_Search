from rest_framework import serializers
from .models import Shed_registration,FormData

class ShedRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shed_registration
        fields = '__all__'




class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ('name', 'age')
