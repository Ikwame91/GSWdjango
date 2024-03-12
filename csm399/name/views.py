from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Memeber

# Create your views here.
def names(request):
    mynames= Memeber.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mynames': mynames
    }
    return HttpResponse(template.render(context,request))


def index(response):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def kwame(response):
    return HttpResponse("<h1> He's a boy who likes walking</h1>")
