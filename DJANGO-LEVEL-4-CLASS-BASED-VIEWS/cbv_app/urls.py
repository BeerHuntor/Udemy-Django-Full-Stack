from django.urls import path
from cbv_app.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
]
