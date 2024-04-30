from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def show_review_view(request):

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            print(review_form.cleaned_data)
            review_form.save(ReviewForm())
            return redirect(reverse('thank_you'))
    else:
        review_form = ReviewForm()
        return render(request, "forms_app/review.html", context={'review_form': review_form})

def show_thank_you_view(request):
    return render (request, "forms_app/thank-you.html")

