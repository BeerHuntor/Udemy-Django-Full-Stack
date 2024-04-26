from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length= 30, required=False)
    last_name = forms.CharField(label='Last Name', max_length= 30, required=False)
    email = forms.EmailField(label='Email', required=False)
    review_contnet = forms.CharField(label='Tell us what you think.', required=False)