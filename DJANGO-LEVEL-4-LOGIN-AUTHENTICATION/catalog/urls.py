from django.urls import path
from catalog.views import CatalogHomeView, BookCreate, BookDetail, my_view

urlpatterns = [
    path('', CatalogHomeView, name='catalog_home'),
    path('create_book/', BookCreate.as_view(), name='create_book'),
    path('book_detail/<slug:slug>/', BookDetail.as_view(), name='book_detail'),
    path('my_view/', my_view, name='my_view'),    
]
