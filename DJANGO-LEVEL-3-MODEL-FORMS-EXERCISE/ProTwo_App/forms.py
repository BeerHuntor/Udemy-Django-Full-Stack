from django.forms import ModelForm
from ProTwo_App.models import User

class UserModelForm(ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"
