from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context ={
        "mymembers":mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().order_by('-lastname', '-id').values()
    template = loader.get_template('template.html')
    
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Descending Order
# By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:

# Example
# Order the result firstname descending:

# mydata = Member.objects.all().order_by('-firstname').values()



# Multiple Order Bys
# To order by more than one field, separate the fieldnames with a comma in the order_by() method:

# Example
# Order the result first by lastname ascending, then descending on id:

# mydata = Member.objects.all().order_by('lastname', '-id').values()
# lastname ascending id descending

# def testing(request):
#     mymembers = Member.objects.filter(firstname__startswith ="L").values()
#     template = loader.get_template('template.html')
    
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     mymembers = Member.objects.filter(Q(firstname="Kwame")| Q(firstname ="Felicia"))
#     template = loader.get_template('template.html')
    
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))