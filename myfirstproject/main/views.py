from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# http request and show som stuff on our website

def index(response, id):
    return HttpResponse("<h1>%s</h1>" %id)
