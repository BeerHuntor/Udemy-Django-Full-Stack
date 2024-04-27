from django.urls import path
from django_forms_app.views import show_review_view, show_thank_you_view

urlpatterns = [
    path('', show_review_view, name='review'),
    path('thanks/', show_thank_you_view, name='thank_you'),
]
