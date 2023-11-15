from rest_framework import serializers
from .models import *

class InventorySerializer(serializers.ModelSerializer):

    crop_type_name = serializers.SerializerMethodField()

    def get_crop_type_name(self, obj):
        return obj.crop_type.name

    class Meta:
        model = Inventory
        fields = ['add_or_remove', 'crop_type_name','crop_price_per_kg', 'crop_quantity','created_at' ]

        # fields = ['id', 'add_or_remove', 'crop_price_per_kg', 'crop_quantity', 'total_crops', 'crop_type_name','created_at', 'crop_type', ]



class MasterInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= MasterInventory
        fields = '__all__'
