from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

template_dir = 'inventory_app/'
# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request, 'inventory_app/list.html', context = context)

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            print('car deleted!')
            return redirect(reverse('inventory_app:list_cars'))
            
        except:
            print('PK not found')
            return redirect(reverse('inventory_app:list_cars'))
    else:   
        return render(request, 'inventory_app/delete.html')

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('inventory_app:list_cars'))
    else:
        return render(request, 'inventory_app/add.html')