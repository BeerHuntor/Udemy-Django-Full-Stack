from django import forms
from .models import Review
from django.forms import ModelForm, NumberInput
from django.core.validators import MaxValueValidator, MinValueValidator

#class ReviewForm(forms.Form):
#    first_name = forms.CharField(label='First Name', max_length= 30, required=False)
#    last_name = forms.CharField(label='Last Name', max_length= 30, required=False)
#    email = forms.EmailField(label='Email', required=False)
#    review_contnet = forms.CharField(label='Tell us what you think.', required=False,
#                                     widget=forms.Textarea(attrs={'class': 'myform', 'rows': '10','cols':'120', 'placeholder': "Text goes here!"}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'email', 'star_rating', 'review_content'] # another way for this, (giving all options available) = '__all__'
        widgets = {
            'star_rating' : NumberInput(attrs={'min':0, 'max':5}),
        }
        # A way to input your own errors to show as {{field.errors}} in the html. 
        error_messages = {
            'star_rating' : {
                'min_value' : "You idiot the min value is 0",
                'max_value' : "nice try buddy, max value is 5!",
            }
        }
        
    
