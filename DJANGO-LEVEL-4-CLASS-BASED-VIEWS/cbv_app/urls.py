from django.urls import path
from cbv_app.views import HomeTemplateView, ThankYouTemplateView, ContactFormView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('thank_you/', ThankYouTemplateView.as_view(), name='thank_you')
]
