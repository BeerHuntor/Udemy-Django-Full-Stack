from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.hmtml
    return render(request, 'my_app/example.html')

def example_variables(request):
    my_var = {'first_name':'Rosalind', "last_name":"Franklin", 
              'some_list':[1,2,3], 'some_dict':{'inside_key' : 'outside_value'}}
    

    return render(request, 'my_app/variables.html', context=my_var)