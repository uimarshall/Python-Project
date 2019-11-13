from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Func to handle traffic frm our homepage
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
def about(request):
    return HttpResponse('<h1>Blog About</h1>')