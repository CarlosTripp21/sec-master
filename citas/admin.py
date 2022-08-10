from django.contrib import admin

from .models import Car, Agenda, Customer

# Register your models here.
admin.site.register(Car)
admin.site.register(Agenda)
admin.site.register(Customer)
