from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def home_page_view(request):
    return HttpResponse("HOME PAGE")