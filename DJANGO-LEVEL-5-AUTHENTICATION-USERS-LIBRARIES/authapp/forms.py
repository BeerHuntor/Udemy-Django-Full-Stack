from django import forms 
from django.contrib.auth.models import User
from authapp.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=25,required=True)
    username = forms.CharField(max_length=50)

    class Meta():
        model = User
        fields = ('username', 'password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)
    
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_picture')
 
