from django.db import models

# Create your models here.
class Car(models.Model):
    vin = models.CharField(max_length=255, unique = True)
    
    def __str__(self):
        return self.vin


class Customer(models.Model):
    curp = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name


class Agenda(models.Model):
    appoinment = models.DateTimeField(null=False)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    customer = models.ForeignKey(Customer, to_field='curp', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.appoinment)
