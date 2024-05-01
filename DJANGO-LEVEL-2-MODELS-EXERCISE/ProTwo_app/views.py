from django.shortcuts import render
from ProTwo_app.models import Users

# Create your views here.
def index_view(request):
    return render(request, 'app/index.html')

def help_view(request):
    return render(request, 'app/help.html')

def users_view(request):
    all_users = Users.objects.all()
    users = {'users_view' : all_users}
    return render(request, 'app/users.html', context=users)