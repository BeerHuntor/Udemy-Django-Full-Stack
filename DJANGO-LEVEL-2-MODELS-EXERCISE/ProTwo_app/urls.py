from django.urls import path
from .views import index_view, help_view, users_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('help/', help_view, name='help_view'),
    path('users/', users_view, name='users_view')
]
