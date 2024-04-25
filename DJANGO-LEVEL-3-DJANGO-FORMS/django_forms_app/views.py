from django.shortcuts import render

# Create your views here.
def show_rental_review(request):
    return render(request, 'app_templates/rental-review.html')

def show_thank_you(request):
    return render(request, 'app_templates/thank-you.html')