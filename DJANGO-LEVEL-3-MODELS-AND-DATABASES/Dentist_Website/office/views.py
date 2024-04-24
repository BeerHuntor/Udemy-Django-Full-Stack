from django.shortcuts import render
import os
from . import models

BASE_DIR = '/Dentist_Website/'
# Create your views here.
def list_patients(request):
    all_patients = models.Patient.objects.all()
    context = {'patients':all_patients}
    return render(request, 'office/list.html', context=context )