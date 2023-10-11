from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name = models.TextField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe/")


class TestTable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    def __str__(self) -> str:
        return f"{self.name} : {self.age}"
    


