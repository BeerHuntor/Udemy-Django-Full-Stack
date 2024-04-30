from django import forms

class ReviewForm(forms.Form):

    first_name = forms.CharField(30)
    last_name = forms.CharField(30)

    review_detail = forms.Textarea
