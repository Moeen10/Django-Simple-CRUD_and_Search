from django.db import models

from shed.models import Shed_registration 
# Create your models here.
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
    def __str__(self):
        return f"{self.cattle_id} - {self.gender}"
    



class MilkYield(models.Model):
        cow = models.ForeignKey(CowRegistration, on_delete=models.CASCADE, related_name='milk_yields')
        date = models.DateField()
        milk_produced = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

        def __str__(self):
            return f"{self.cow.cattle_id} - {self.date} - {self.milk_produced} liters"