from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello World</h1>")

def kwame(response):
    return HttpResponse("<h1> He's a boy who likes walking</h1>")
