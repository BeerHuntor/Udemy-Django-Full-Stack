from django.shortcuts import render

# Create your views here.
def CatalogHomeView(request):
    return render(request, 'catalog/index.html')