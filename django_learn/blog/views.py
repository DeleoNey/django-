from django.shortcuts import render
from blog.models import Post

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-title')[:99999],
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
