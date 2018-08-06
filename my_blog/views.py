from django.shortcuts import render
from .models import Posts
# Create your views here.
def index(request):
    posts= Posts.objects.all()
    context={
        "title":'My latest Post',
        "posts":posts

    }
    
    return render(request, 'index.html', context)

def details(request, id):
    post=Posts.objects.get(id=id)
    context = {
        "post":post
    }

    return render(request, 'details.html', context)