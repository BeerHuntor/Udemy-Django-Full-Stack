from django.shortcuts import render
from . import models

template_dir = 'inventory_app/'
# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request, 'inventory_app/list.html', context = context)

def delete(request):
    return render(request, 'inventory_app/delete.html')

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
    return render(request, 'inventory_app/add.html')