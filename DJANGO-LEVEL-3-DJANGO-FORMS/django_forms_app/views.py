from django.shortcuts import render

# Create your views here.
def show_review_view(request):
    return render(request, "forms_app/review.html")

def show_thank_you_view(request):
    return render (request, "forms_app/thank-you.html")
