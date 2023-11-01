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
    class Meta:
        model = CowRegistration
        fields = '__all__'
        # fields = ("cattle_id","age","color","date_of_birth")

    #     shed = models.ForeignKey(Shed_registration, on_delete=models.CASCADE ,related_name='CowRegistration')
    # cattle_id = models.CharField(max_length=10, unique=True)
    # origin = models.CharField(max_length=10, choices=ORIGIN_CHOICES)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # age = models.PositiveIntegerField()
    # date_of_birth = models.DateField()
    # color = models.CharField(max_length=50)
    # breeding_rate = models.DecimalField(max_digits=4, decimal_places=2)
    # weight = models.DecimalField(max_digits=5, decimal_places=2)
    # milk_yield = models.DecimalField(max_digits=5, decimal_places=2)
    # active = models.BooleanField(choices=ACTIVE_CHOICES)
    # desease = models.ForeignKey(MasterDesease, on_delete=models.CASCADE ,related_name='CowDesease')
    # medicine = models.ForeignKey(MasterMedicin, on_delete=models.CASCADE ,related_name='CowMedicine')
    # vaccine 