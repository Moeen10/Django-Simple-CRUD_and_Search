from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'crop_type',
        'crop_price_per_kg',
        'crop_quantity',
        'add_or_remove',
        'total_crops',
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('crop_type', 'shed_supply', 'quantity_sold','date')
    def crop_type(self, obj):
        return obj.crop.crop_type
    crop_type.short_description = 'Crop Type'



@admin.register(MasterInventory)
class MasterInventoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'name_bangla',
        'unit_price', 
        'description',
        'description_bangla' 
    ]

    ordering = ('-created_at',)



@admin.register(RemainingInventory)
class RemainingInventoryAdmin(admin.ModelAdmin):
    list_display = [
        'inventory_item',
        'total_quantity',
    ]