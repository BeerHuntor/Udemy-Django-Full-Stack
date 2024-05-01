from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'app/index.html')

def sign_up_view(request):
    return render(request, 'app/users.html')

def help_view(request):
    return render(request, 'app/help.html')