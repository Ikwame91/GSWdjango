from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item
# Create your views here.

# http request and show som stuff on our website

def index(response):
    return HttpResponse("hello")
