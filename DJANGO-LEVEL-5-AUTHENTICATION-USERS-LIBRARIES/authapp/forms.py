from django import forms 
from authapp.models import UserProfileInfo

class USerProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)
    
    class Meta():
        model = UserProfileInfo
        exclude = ('user')
