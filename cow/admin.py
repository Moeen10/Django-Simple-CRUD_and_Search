from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(CowRegistration)
class CowRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'cattle_id' ,
        'origin',
        'gender' ,
        'age' ,
        'date_of_birth',
        'color' ,
        'breeding_rate' ,
        'weight',
        'milk_yield'
    ]



@admin.register(MilkYield)
class MilkYieldAdmin(admin.ModelAdmin):
    list_display = ('cow_cattle_id', 'date', 'milk_produced')

    def cow_cattle_id(self, obj):
        return obj.cow.cattle_id
    cow_cattle_id.short_description = 'Cow Cattle ID'