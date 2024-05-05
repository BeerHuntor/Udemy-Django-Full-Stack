from django.urls import path
from authapp.views import show_index_view, show_login_view, show_logout_view, RegisterFormView

APP_NAME = 'authapp'

urlpatterns = [
    path('', show_index_view, name='index'),
    path('login/', show_login_view, name='login'), 
    path('register/', RegisterFormView.as_view(), name='register'),
    path('logout/',show_logout_view, name='logout'),
]
