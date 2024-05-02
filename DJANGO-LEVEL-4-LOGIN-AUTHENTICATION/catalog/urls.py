from django.urls import path
from catalog.views import CatalogHomeView

urlpatterns = [
    path('', CatalogHomeView, name='catalog_home'),
    
]
