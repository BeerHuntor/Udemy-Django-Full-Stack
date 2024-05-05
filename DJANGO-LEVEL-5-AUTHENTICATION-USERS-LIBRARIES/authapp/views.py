from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import request
from django.views.generic.edit import FormView
from authapp.models import User, UserProfileInfo
from authapp.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import logout
# Create your views here.
def show_index_view(request):
    return render(request, 'authapp/index.html')

def show_login_view(request):
    return render(request, 'authapp/login.html')

def show_logout_view(request):
    logout(request)
    return render (request, 'index')

class RegisterFormView(FormView):
    form_class = UserForm
    other_form_class = UserProfileInfoForm

    def get_template_names(self): 
        return ['authapp/registration.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.form_class
        context['profile_form'] = self.other_form_class
        return context
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    def form_valid(self, form):
        # Save the user data
        user = form.save()

        #Get the UserProfileInfoForm data
        profile_form = self.other_form_class(self.request.POST)

        # Check if the profile data is valid
        if profile_form.is_valid():
            # Save the profile data
            profile = profile_form.save(commit=False)
            profile.user = user # Linking the profile to the user. 
            profile.save()

            # We get the files in the request.FILES and then do something with it. In this case, we set their profile pic to the one uploaded. 
            if 'profile_pic' in self.request.FILES:
                profile.profile_pic = self.request.FILES['profile_pic']
            return super().form_valid(form)
        else:
            print(self.user_form.errors, self.profile_form.errors)