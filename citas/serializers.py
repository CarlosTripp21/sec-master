from rest_framework import serializers
from .models import Car, Customer, Agenda


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "pk",
            "vin",
        ]
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "pk",
            "curp",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {
            "first_name" : {"required" : False},
            "last_name" : {"required" : False},
        }

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = [
            "pk",
            "appoinment",
            "created",
            "modified",
            "customer",
        ]
        extra_Kwargs = {
            "appoinment" : {"required" : False},
            "created" : {"required" : False},
            "modified" : {"required" : False},
            "customer" : {"required" : False},
        }