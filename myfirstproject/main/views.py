from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item
# Create your views here.

# http request and show som stuff on our website


def index(response, id):
    ls = TodoList.objects.get(id=id)
    item = ls.item_set.get(id=id)
    return HttpResponse()

def home(response):
    return HttpResponse("hello")
