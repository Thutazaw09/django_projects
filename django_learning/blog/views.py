from django.shortcuts import render
from django.http import  HttpRequest
# Create your views here.

# mock data
posts = [
    {
        'author': 'AgAge',
        'title': 'Sleep',
        'content': 'First post content',
        'data_posted': 'August 27,2018',
    },
    {
        'author': 'MgMg',
        'title': 'Sleep',
        'content': 'First post content',
        'data_posted': 'August 27,2018',
    },
]


def home(request: HttpRequest):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request: HttpRequest):
    return render(request, 'blog/about.html')
