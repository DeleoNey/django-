from django.shortcuts import render

posts = [
    {
        'author': 'Max',
        'title': 'My First Post',
        'content': 'My first post content',
        'date_posted': 'August 11, 2025',
    },
    {
        'author': 'Andrii',
        'title': 'My First Post',
        'content': 'My first post content',
        'date_posted': 'August 11, 2025',
    },
    {
        'author': 'Petro',
        'title': 'Post about cats',
        'content': 'Cats are cute',
        'date_posted': 'August 08, 2025',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
