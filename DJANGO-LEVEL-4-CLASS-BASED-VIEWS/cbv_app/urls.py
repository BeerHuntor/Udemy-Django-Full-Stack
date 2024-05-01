from django.urls import path
from cbv_app.views import HomeTemplateView, ThankYouTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('thank_you/', ThankYouTemplateView.as_view(), name='thank_you')
]
