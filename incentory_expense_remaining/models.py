from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from django.utils import timezone
# Model to track the inventory of crops


class MasterInventory(models.Model):
    name = models.CharField(max_length=50 )
    name_bangla = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    description_bangla = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_inventory_set')

    def __str__(self):
        return f"{self.name} ({self.name_bangla})"
    class Meta:
        db_table = 'm_inventory_type'



class Inventory(models.Model):
    crop_type = models.ForeignKey(MasterInventory, on_delete=models.CASCADE)
    add_or_remove = models.CharField(max_length=10)
    crop_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    crop_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_crops =  models.DecimalField(max_digits=10, decimal_places=2,default=0, )
    created_at  = models.DateField(default=timezone.now)

    def __str__(self):
        return self.crop_type.name + f'({self.crop_type.name_bangla})'
    
    class Meta:
        db_table = 'innnvventory'


  # Model to track the individual history of remaining crops
class RemainingInventory(models.Model):
    inventory_item = models.ForeignKey(MasterInventory, on_delete=models.CASCADE)
    total_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f" {self.inventory_item} remains {self.total_quantity}"

    class Meta:
        verbose_name = "Remaining Inventory"
        verbose_name_plural = "Remaining Inventories"
        db_table = 'remaining_inventory'


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



