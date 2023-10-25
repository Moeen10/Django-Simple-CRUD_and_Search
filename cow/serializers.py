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