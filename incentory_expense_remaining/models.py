from django.db import models
from django.core.exceptions import ValidationError
# Model to track the inventory of crops
class Inventory(models.Model):
    crop_type = models.CharField(max_length=100, unique=True)
    crop_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    crop_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.crop_type

# Model to track expenses and sold crops
class Expense(models.Model):
    crop = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    shed_supply = models.CharField(max_length=100,default="Shed 1")
    quantity_sold = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.shed_supply} - {self.crop.crop_type}"
    
    def save(self, *args, **kwargs):
        if self.quantity_sold > self.crop.crop_quantity:
            raise ValidationError("Quantity sold cannot be greater than the total inventory quantity.")
        super().save(*args, **kwargs)    

# Model to track the individual history of remaining crops
class RemainingCrops(models.Model):
    crop = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.crop.crop_type
