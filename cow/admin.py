from django.contrib import admin
from .models import *

from django.forms import ModelForm
from django.forms import ModelChoiceField
# Register your models here.

@admin.register(MasterDesease)
class MasterDeseaseAdmin(admin.ModelAdmin):
  list_display = ('desease_name','desease_description')
  
    
    
@admin.register(MasterVaccine)
class MasterVaccineAdmin(admin.ModelAdmin):
  list_display = ('desease','vaccine_name','vaccine_details')
  def desease(self,obj):
    return obj.desease.desease_name
  desease.short_description = 'Desease'


@admin.register(MasterMedicin)
class MasterMedicinAdmin(admin.ModelAdmin):
  list_display = ('desease','medicine_name','medicine_details')
  def desease(self,obj):
    return obj.desease.desease_name
  desease.short_description = 'Desease'




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



@admin.register(Sick_Cow)
class Sick_CowAdmin(admin.ModelAdmin):
   list_display = ( 'cow_desease' , 'cow_id')
   def cow_desease(self,obj):
    return obj.cow_desease.desease_name
   cow_desease.short_description = 'Desease Name'


    

# class CowRegistrationAdminForm(ModelForm):
#     class Meta:
#         model = CowRegistration
#         fields = '__all__'

#     vaccine = ModelChoiceField(
#         queryset=MasterVaccine.objects.all(),
#         label='Vaccine',
#         to_field_name='vaccine_name',
#         empty_label='Select a vaccine',
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Filter the vaccine choices by the selected disease.
#         if self.instance.disease:
#             self.fields['vaccine'].queryset = MasterVaccine.objects.filter(desease=self.instance.disease)

# class CowRegistrationAdmin(admin.ModelAdmin):
#     form = CowRegistrationAdminForm

#     list_display = ('cattle_id', 'gender', 'age', 'vaccine')
# admin.site.register(CowRegistration, CowRegistrationAdmin)

@admin.register(MilkYield)
class MilkYieldAdmin(admin.ModelAdmin):
    list_display = ('cow_cattle_id', 'date', 'milk_produced')

    def cow_cattle_id(self, obj):
        return obj.cow.cattle_id
    cow_cattle_id.short_description = 'Cow Cattle ID'