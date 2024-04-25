from django.urls import path
from . import views

app_name = 'inventory_app'

urlpatterns = [
    path('',  views.list, name="list_cars"),
    path('delete/', views.delete, name="delete_cars"),
    path('add/', views.add, name="add_cars"),    
]
