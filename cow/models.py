from django.db import models
from django.contrib.auth.models import User
from shed.models import Shed_registration 
# Create your models here.

class MasterDesease(models.Model):
    desease_name = models.CharField(max_length=100)
    desease_description = models.TextField()
    desease_description_bangla = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_desease_set')

    def __str__(self):
         return f"{self.desease_name}"
    
    class Meta:
        db_table = 'm_desease'



class MasterMedicin(models.Model):
    desease = models.ForeignKey(MasterDesease, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    medicine_details = models.TextField()
    medicine_details_bangla = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_mastermedicine_set')

    def __str__(self):
        return f"{self.medicine_name}"
    
    class Meta:
        db_table = 'm_medicine'


class MasterVaccine(models.Model):
    desease = models.ForeignKey(MasterDesease, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    vaccine_details = models.TextField()
    vaccine_details_bangla = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_mastervaccine_set')

    def __str__(self):
        return f"{self.vaccine_name}"
    
    class Meta:
        db_table = 'm_vaccine'




class CowRegistration(models.Model):
    ORIGIN_CHOICES = (
        ('Local', 'Local'),
        ('Imported', 'Imported'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    ACTIVE_CHOICES = (
        (True , 'Yes'),
        (False , 'No'),
    )
    shed = models.ForeignKey(Shed_registration, on_delete=models.CASCADE ,related_name='CowRegistration')
    cattle_id = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=10, choices=ORIGIN_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    color = models.CharField(max_length=50)
    breeding_rate = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    milk_yield = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(choices=ACTIVE_CHOICES)
    desease = models.ForeignKey(MasterDesease, on_delete=models.CASCADE ,related_name='CowDesease')
    medicine = models.ForeignKey(MasterMedicin, on_delete=models.CASCADE ,related_name='CowMedicine')
    vaccine = models.ForeignKey(MasterVaccine, on_delete=models.CASCADE, related_name='CowVaccine')
    def __str__(self):
        return f"{self.cattle_id} - {self.gender}"
    



class MilkYield(models.Model):
        cow = models.ForeignKey(CowRegistration, on_delete=models.CASCADE, related_name='milk_yields')
        date = models.DateField()
        milk_produced = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

        def __str__(self):
            return f"{self.cow.cattle_id} - {self.date} - {self.milk_produced} liters"
        

