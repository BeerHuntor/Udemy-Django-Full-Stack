from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help_view(request):
    help_page = {'help' : 'help page'}
    return render (request, 'my_app/help.html', context=help_page)