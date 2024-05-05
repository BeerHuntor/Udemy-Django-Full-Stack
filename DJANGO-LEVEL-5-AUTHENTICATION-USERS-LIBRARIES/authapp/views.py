from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from authapp.models import User, UserProfileInfo
from authapp.forms import UserForm, UserProfileInfoForm
# Create your views here.
def show_index_view(request):
    return render(request, 'authapp/index.html')

def show_login_view(request):
    return render(request, 'authapp/login.html')

class RegisterFormView(FormView):
    form_class = UserForm
    other_form_class = UserProfileInfoForm
    success_url = '/'   

    def get_template_names(self): 
        return ['authapp/registration.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.form_class
        context['profile_form'] = self.other_form_class
        return context
    
    def get_success_url(self):
        return reverse_lazy('register')