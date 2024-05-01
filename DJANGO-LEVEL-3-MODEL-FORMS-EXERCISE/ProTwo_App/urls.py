from django.urls import path
from ProTwo_App.views import index_view, sign_up_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('users/', sign_up_view, name='sign_up_view'),
]
