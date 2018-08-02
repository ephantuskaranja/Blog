from django.shortcuts import render

# Create your views here.
def index(request):
    
    context={
        "title":'My latest Post',

    }
    
    return render(request, 'index.html', context)