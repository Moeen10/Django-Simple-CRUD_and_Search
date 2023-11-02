from rest_framework import serializers
from .models import *

class AllCowSerializer(serializers.ModelSerializer):
    crop_type_name = serializers.SerializerMethodField()

    def get_crop_type_name(self, obj):
        return obj.crop_type.name
    class Meta:
        model = CowRegistration
        fields = '__all__'


    
class MasterDeseaseSerializer(serializers.ModelSerializer):
        class Meta:
            model = MasterDesease
            fields = ("id","desease_name","desease_description","desease_description_bangla")


class MasterVaccineSerializer(serializers.ModelSerializer):
        class Meta:
            model = MasterVaccine
            fields = ("id" , "vaccine_name" , "vaccine_details" , "vaccine_details_bangla")

class MasterMedicinSerializer(serializers.ModelSerializer):
        class Meta:
            model = MasterMedicin
            fields = ("id" ,"medicine_name","medicine_details", "medicine_details_bangla")


class DisplayAllCowSerializer(serializers.ModelSerializer):
     class Meta:
          model:CowRegistration
          fields = '__all__'


class CowRegistrationSerializer(serializers.ModelSerializer):
    
    # desease_name = serializers.ListSerializer(child=serializers.CharField())
    desease = serializers.StringRelatedField(many=True)
    medicine = serializers.StringRelatedField(many=True)
    vaccine = serializers.StringRelatedField(many=True)
    class Meta:
        model = CowRegistration
        fields = '__all__'



