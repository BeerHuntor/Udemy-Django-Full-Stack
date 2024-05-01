from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView

from cbv_app.forms import ContactForm

from cbv_app.models import Teacher
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'app/index.html'

class ThankYouTemplateView(TemplateView):
    template_name = 'app/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "app/contact.html"

    success_url = reverse_lazy('thank_you')# This is a URL as in your browser, not a pattern/pointer.

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html

    fields = '__all__'
    success_url = reverse_lazy('thank_you')


    def get_template_names(self): # Changes where CreateView looks for the templates by default, by overriding the method call. 
        return ['app/teacher_form.html', 'app/model_form.html']
    

class TeacherListView(ListView):

    #model_list.html
    model = Teacher

    def get_template_names(self):
        return ['app/teacher_list.html', 'app/teacher_list.html']