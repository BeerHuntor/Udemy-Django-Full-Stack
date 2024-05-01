from django.urls import path
from cbv_app.views import HomeTemplateView, ThankYouTemplateView, ContactFormView, TeacherCreateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('thank_you/', ThankYouTemplateView.as_view(), name='thank_you'),
    path('teacher/', TeacherCreateView.as_view(), name='teacher_form'),
]
