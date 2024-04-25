from django.contrib import admin
from inventory_app.models import Car

# Register your models here.

#One liner if you don't need the model class object. 
#admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME_INFORMATION', {'fields':['year']}), 
        ('CAR_INFORMATION', {'fields':['brand']}),
    ]
admin.site.register(Car, CarAdmin)