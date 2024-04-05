from django.urls import path
from . import views


app_name = "my_app"

urlpatterns = [
    path('', views.example_view, name='example'), 
    path('variables/', views.example_variables, name='variable'),
]
