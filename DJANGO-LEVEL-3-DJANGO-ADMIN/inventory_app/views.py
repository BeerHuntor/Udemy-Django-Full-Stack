from django.shortcuts import render

template_dir = 'inventory_app/'
# Create your views here.
def list(request):
    return render(request, 'inventory_app/list.html')

def delete(request):
    return render(request, 'inventory_app/delete.html')

def add(request):
    return render(request, 'inventory_app/add.html')