from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'app/index.html'

class ThankYouTemplateView(TemplateView):
    template_name = 'app/thank_you.html'