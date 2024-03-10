from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# http request and show som stuff on our website

def index(response):
    return HttpResponse("<h1>Hello World of coders</h1>")

def f1(response):
    return HttpResponse("<h1>Do You eat Bread Baby girl</h1>")