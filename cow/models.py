from django.db import models
from django.contrib.auth.models import User
from shed.models import Shed_registration 
from django.utils import timezone
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

    VACCINE_DOSR = (

        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
    )

    HELTH_STATUS = (
        ("Good","Good"),
        ("Sick","Sick"),
        ("Natural","Natural"),
    )

    HEAT_STATUS = (
        ("No","No"),
        ("Yes","Yes"),
    )

    SEMEN_PUSH_STATUS = (
        ("No","No"),
        ("Yes","Yes"),
    )

    DELICERY_STATUS = (
        ("No","No"),
        ("Yes","Yes"),
    )
    

    shed = models.ForeignKey(Shed_registration, on_delete=models.CASCADE ,related_name='CowRegistration',default=1)
    cattle_id = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=10,)
    gender = models.CharField(max_length=10,)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    color = models.CharField(max_length=50)
    breeding_rate = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    milk_yield = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(choices=ACTIVE_CHOICES)
    desease = models.ManyToManyField(MasterDesease ,related_name='CowDesease' ,blank=True)
    medicine = models.ManyToManyField(MasterMedicin,related_name='CowMedicine',blank=True)
    vaccine = models.ManyToManyField(MasterVaccine, related_name='CowVaccine',blank=True)
 

    helth_status = models.CharField(max_length=30 , choices = HELTH_STATUS , default="Natural", )
    current_vaccine_dose = models.DecimalField(max_digits=4, decimal_places=2 , default=0)
    next_vaccine_dose = models.DateField(default=timezone.now)


    provable_heat_date = models.DateField(default=timezone.now)
    heat_status = models.CharField(max_length=10, choices=HEAT_STATUS , default="No")
    actual_heat_date = models.DateField(default=timezone.now)
    semen_push_status = models.CharField(max_length=10, choices=SEMEN_PUSH_STATUS , default="No")
    pregnant_date = models.DateField(default=timezone.now)
    delivery_status = models.CharField(max_length=10,choices=DELICERY_STATUS ,  default="No")
    delivery_date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"{self.cattle_id} - {self.gender}"
    


class Sick_Cow(models.Model):
    cow_desease = models.ForeignKey(MasterDesease,on_delete=models.PROTECT , related_name='SickCowDesease')
    cow_id = models.ForeignKey(CowRegistration, on_delete=models.PROTECT , related_name='SeickCowID' )


    def __str__(self):
        return f"Sick Cow Id : {self.cow_id} ans Desease is : {self.cow_desease.desease_name}"




class MilkYield(models.Model):
        cow = models.ForeignKey(CowRegistration, on_delete=models.CASCADE, related_name='milk_yields')
        date = models.DateField()
        milk_produced = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

        def __str__(self):
            return f"{self.cow.cattle_id} - {self.date} - {self.milk_produced} liters"