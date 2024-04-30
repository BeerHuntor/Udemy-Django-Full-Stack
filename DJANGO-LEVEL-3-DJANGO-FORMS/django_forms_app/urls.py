from django.urls import path
<<<<<<< HEAD
from django_forms_app.views import show_rental_review, show_thank_you

urlpatterns = [
    path('', show_rental_review, name='rental_review'),
    path('thank-you/', show_thank_you, name='thank_you'),
=======
from django_forms_app.views import show_review_view, show_thank_you_view

urlpatterns = [
    path('', show_review_view, name='review'),
    path('thanks/', show_thank_you_view, name='thank_you'),
>>>>>>> refs/remotes/origin/main
]
