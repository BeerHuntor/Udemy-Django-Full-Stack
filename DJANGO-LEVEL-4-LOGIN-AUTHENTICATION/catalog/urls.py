from django.urls import path
from catalog.views import CatalogHomeView, BookCreate, BookDetail, my_view, SignUpView, CheckedOutBooksByUser

urlpatterns = [
    path('', CatalogHomeView, name='catalog_home'),
    path('create_book/', BookCreate.as_view(), name='create_book'),
    path('book_detail/<slug:slug>/', BookDetail.as_view(), name='book_detail'),
    path('my_view/', my_view, name='my_view'),
    path('signup/', SignUpView.as_view(), name="sign_up"),
    path('profile/', CheckedOutBooksByUser.as_view(), name='profile'),    
]
