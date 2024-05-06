from django.urls import path
from authapp.views import show_index_view, show_login_view, show_logout_view, RegisterFormView

app_name = 'authapp'

urlpatterns = [
    path('', show_index_view, name='index'),
    path('login/', show_login_view, name='login'), 
    path('logout/',show_logout_view, name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),

]
