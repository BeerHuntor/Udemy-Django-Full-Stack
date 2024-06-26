from django.urls import path
from cbv_app.views import HomeTemplateView, ThankYouTemplateView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailedView, TeacherUpdateView, TeacherDeleteView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('thank_you/', ThankYouTemplateView.as_view(), name='thank_you'),
    path('teacher/', TeacherCreateView.as_view(), name='teacher_form'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', TeacherDetailedView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>', TeacherUpdateView.as_view(), name='teacher_update'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher'),
    
]
