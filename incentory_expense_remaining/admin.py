from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = [
        'crop_type',
        'crop_price_per_kg',
        'crop_quantity'
     ]

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('crop_type', 'shed_supply', 'quantity_sold','date')
    def crop_type(self, obj):
        return obj.crop.crop_type
    crop_type.short_description = 'Crop Type'


@admin.register(RemainingCrops)
class RemainingCropsAdmin(admin.ModelAdmin):
    list_display = []