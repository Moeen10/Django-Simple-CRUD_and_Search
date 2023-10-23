from rest_framework import serializers
from .models import CowRegistration

class AllCowSerializer(serializers.ModelSerializer):
    crop_type_name = serializers.SerializerMethodField()

    def get_crop_type_name(self, obj):
        return obj.crop_type.name
    class Meta:
        model = CowRegistration
        fields = '__all__'


    
     