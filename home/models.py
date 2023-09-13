from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(default="Chandpur")


class product(models.Model):
    pass