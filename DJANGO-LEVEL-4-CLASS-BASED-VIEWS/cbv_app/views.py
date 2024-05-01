from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from cbv_app.forms import ContactForm
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'app/index.html'

class ThankYouTemplateView(TemplateView):
    template_name = 'app/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "app/contact.html"

    success_url = '/thank_you/'# This is a URL as in your browser, not a pattern/pointer.

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    