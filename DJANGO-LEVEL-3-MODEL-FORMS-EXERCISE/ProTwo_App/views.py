from django.shortcuts import render, redirect
from ProTwo_App.forms import UserModelForm

# Create your views here.
def index_view(request):
    return render(request, 'app/index.html')

def sign_up_view(request):
    if request.method == "POST":
        form = UserModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index_view')
        
    else:
        form = UserModelForm()
        return render(request, 'app/users.html', {'form':form})

def help_view(request):
    return render(request, 'app/help.html')