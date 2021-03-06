from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Supplier(models.Model):
    supplier_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20, blank = True)
    email = models.EmailField(max_length = 254, blank = True)
    description = models.CharField(max_length = 80, blank=True)
    class Meta:
        db_table = "Supplier"
    def __str__(self):
      return self.supplier_name

class Purchasing(models.Model):
    purchasing_id = models.AutoField(primary_key=True)
    pv_no = models.CharField(max_length = 200)
    invoice_no = models.CharField(max_length = 200, blank=True)
    purchasing_date = models.DateField(default=timezone.now, blank=True)
    description = models.CharField(max_length = 100, blank=True)
    class Meta:
        db_table = "Purchasing"
    def __str__(self):
        return self.pv_no

# Abstract class to inherit from 
class Irrigation_Tables(models.Model):
    name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    threshold = models.PositiveIntegerField(default = 0)
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)], blank=True)
    description = models.CharField(max_length = 100, blank=True)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.SET_NULL, null =True, blank=True,)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null =True, blank=True)
    class Meta:
        abstract = True

class Plantation_Tables(models.Model):
    name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    threshold = models.PositiveIntegerField(default = 0)    
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)], blank=True)
    description = models.CharField(max_length = 100, blank=True)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.SET_NULL, blank=True, null =True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null =True, blank=True)
    class Meta:
        abstract = True

class Vehicle_Tables(models.Model):
    
    class Meta:
        abstract = True

class Tools(Plantation_Tables):
    class Meta:
        db_table = "tools"

    def __str__(self):
        return self.name

class Stationery(Plantation_Tables):
    class Meta:
        db_table = "stationery"

    def __str__(self):
        return self.name
class Consumables(Plantation_Tables):
    class Meta:
        db_table = "consumables"

    def __str__(self):
        return self.name

class Fungicide(Plantation_Tables):
    class Meta:
        db_table = "fungicide"

    def __str__(self):
        return self.name

class Fertilizer(Plantation_Tables):
    class Meta:
        db_table = "fertilizer"
    
    def __str__(self):
        return self.name

class Surfacetant(Plantation_Tables):
    class Meta:
        db_table = "surfacetant"

    def __str__(self):
        return self.name

class Herbicide(Plantation_Tables):
    class Meta:
        db_table = "herbicide"

    def __str__(self):
        return self.name

class Pesticide(Plantation_Tables):
    class Meta:
        db_table = "pesticide"
    def __str__(self):
        return self.name
        
class Irrigation(Irrigation_Tables):

    class Meta:
        db_table = "irrigation"
    def __str__(self):
        return self.name

class Vehicle(Vehicle_Tables):
    vehicle_type = models.CharField(max_length = 30)
    vehicle_name = models.CharField(max_length = 50)
    vehicle_number_plate = models.CharField(max_length = 10, blank=True)
    vehicle_owner = models.CharField(max_length = 30, blank=True)
    class Meta:
        db_table = "vehicle"
    def __str__(self):
        return self.vehicle_name

class Spareparts(Vehicle_Tables):
    name = models.CharField(max_length = 30)
    vehicle_assigned = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, blank=True, null =True)
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    quantity = models.PositiveIntegerField(default = 0)
    threshold = models.PositiveIntegerField(default = 0)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.SET_NULL, blank=True, null =True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null =True, blank=True)
    class Meta:
        db_table = "spareparts"
    def __str__(self):
        return self.name