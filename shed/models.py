from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shed_registration(models.Model):
    shedName = models.CharField(max_length=100)
    shedLength = models.FloatField(default=0.0)
    shedWidth = models.FloatField(default=0.0)
    shedLocation = models.TextField(max_length=300)
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField()
    number_of_cow = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sheds')

    def __str__(self) -> str:
        return f"Shed Name -  {self.shedName}  ||  Cow Number - {self.number_of_cow}  ||  User Name - {self.owner.username}"
    
