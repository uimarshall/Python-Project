from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Func to handle traffic frm our homepage

posts = [
    {'author': 'Melin Author', 'title': 'Blog Post1',
        'content': 'First post content', 'post_date': '23 June 2019'},
    {'author': 'Frank Ann', 'title': 'Blog Post2',
        'content': 'Second post content', 'post_date': '6 August 2019'}
]

context = {
    'posts': posts
}


def home(request):
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
