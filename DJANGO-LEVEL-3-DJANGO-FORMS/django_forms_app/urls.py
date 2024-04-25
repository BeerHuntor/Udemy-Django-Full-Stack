from django.urls import path
from django_forms_app.views import show_rental_review, show_thank_you

urlpatterns = [
    path('', show_rental_review, name='rental_review'),
    path('thank-you/', show_thank_you, name='thank_you'),
]
