from django.urls import path
from django_forms_app.views import show_review_view, show_thank_you_view

urlpatterns = [
    path('', show_review_view, name='rental_review'),
    path('thank-you/', show_thank_you_view, name='thank_you'),
]